import asyncio
from os import getenv

from google.oauth2 import service_account
from googleapiclient.discovery import build

loop = asyncio.get_event_loop()
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
credentials = service_account.Credentials.from_service_account_file(
    getenv('SERVICE_ACCOUNT_FILE'), scopes=SCOPES
)
service = build('sheets',
                'v4',
                credentials=credentials,
                cache_discovery=False)
sheet = service.spreadsheets()


async def read_sheet_values(top_right_cell: str, bottom_left_cell: str) -> list:
    """
        Возвращает строки из таблицы с первой по вторую ячейки
    :param top_right_cell: Верхняя правая ячейка области возвращаемых данных
    :param bottom_left_cell: Нижняя левая ячейка области возвращаемых данных
    :return: Список списков. Каждый внутренний список - строка указанной области
    """
    result = await loop.run_in_executor(
        None,
        sheet.values().get(spreadsheetId=getenv('SPREAD_SHEET_ID'),
                           range=f'{getenv("SHEET_NAME")}!{top_right_cell}:{bottom_left_cell}').execute
    )
    return result.get('values', [])