import asyncio

from google.oauth2 import service_account
from googleapiclient.discovery import build

from config import SHEET_ID

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
credentials = service_account.Credentials.from_service_account_file(
    "credentials.json", scopes=SCOPES
)

service = build('sheets',
                'v4',
                credentials=credentials,
                cache_discovery=False)
sheet = service.spreadsheets()


async def read_sheet_values(top_right_cell: str, bottom_left_cell: str) -> list:
    """
        Возвращает строки из таблицы с первой по вторую ячейки. Нотация A1 или нотация R1C1
    :param top_right_cell: Верхняя правая ячейка области возвращаемых данных
    :param bottom_left_cell: Нижняя левая ячейка области возвращаемых данных
    :return: Список списков. Каждый внутренний список - строка указанной области
    """
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        sheet.values().get(spreadsheetId=SHEET_ID,
                           range=f'{top_right_cell}:{bottom_left_cell}').execute # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get?hl=ru#:~:text=%D0%9D%D0%BE%D1%82%D0%B0%D1%86%D0%B8%D1%8F%20A1%20%D0%B8%D0%BB%D0%B8%20%D0%BD%D0%BE%D1%82%D0%B0%D1%86%D0%B8%D1%8F%20R1C1
    )
    return result.get('values', [])


async def get_data():
    r = 1
    c = 1
    data = await read_sheet_values('R1C1', f'R{r}C{c}')
    new_data = [[1]]
    while data != new_data:
        data = new_data
        c += 20
        new_data = await read_sheet_values('R1C1', f'R{r}C{c}')
    data = new_data
    try:
        c = data[0].index('')
    except:
        ...


    new_data = [[1]]
    while data != new_data:
        data = new_data
        r += 20
        new_data = await read_sheet_values('R1C1', f'R{r}C{c}')
    data = new_data
    try:
        data = data[:data.index([])]
    except:
        ...

    return data


async def main():
    print(await get_data())


if __name__ == '__main__':
    asyncio.run(main())