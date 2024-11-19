from tradingview_ta import Analysis, TA_Handler, Interval, Exchange, get_multiple_analysis
from colorama import Fore, Style
from prettytable import PrettyTable


WATCH_LIST = [
    "AUDCAD",
    "AUDCHF",
    "AUDUSD",
    "CADCHF",
    "CADSGD",
    "EURAUD",
    "EURCAD",
    "EURCHF",
    "EURGBP",
    "EURJPY",
    "EURSGD",
    "EURUSD",
    "GBPJPY",
    "GBPUSD",
    "NZDUSD",
    "USDCAD",
    "USDCHF",
    "USDTHB",
    "ZARCHF",
]

# order matters here
TIME_FRAMES = [
    "W1",
    "D1",
    "H4",
    "H1",
    "M30",
    "M15",
]


def get_analysis_for_multiple_timeframes():
    analysis = {}

    for time in TIME_FRAMES:
        if time == "W1":
            analysis["W1"] = get_multiple_analysis(
                screener="forex",
                interval=Interval.INTERVAL_1_WEEK,
                symbols=symbols)
        elif time == "D1":
            analysis["D1"] = get_multiple_analysis(
                screener="forex",
                interval=Interval.INTERVAL_1_DAY,
                symbols=symbols)
        elif time == "H4":
            analysis["H4"] = get_multiple_analysis(
                screener="forex",
                interval=Interval.INTERVAL_4_HOURS,
                symbols=symbols)
        elif time == "H1":
            analysis["H1"] = get_multiple_analysis(
                screener="forex",
                interval=Interval.INTERVAL_1_HOUR,
                symbols=symbols)
        elif time == "M30":
            analysis["M30"] = get_multiple_analysis(
                screener="forex",
                interval=Interval.INTERVAL_30_MINUTES,
                symbols=symbols)
        elif time == "M15":
            analysis["M15"] = get_multiple_analysis(
                screener="forex",
                interval=Interval.INTERVAL_15_MINUTES,
                symbols=symbols)
    return analysis


# add the exchange to all the symbols
symbols = [f"FX_IDC:{symbol}" for symbol in WATCH_LIST]

# Color
R = "\033[0;31;40m"  # RED
G = "\033[90m"  # Grey for Neutral
Y = "\033[0;33;40m"  # Yellow
B = "\033[0;34;40m"  # Blue
N = "\033[0m"  # Reset


table = PrettyTable()

table.add_column("", WATCH_LIST)

all_analysis_data = get_analysis_for_multiple_timeframes()
for timeframe, analysis in all_analysis_data.items():
    column_data = [
        B + value.summary["RECOMMENDATION"] + N
        if "BUY" in value.summary["RECOMMENDATION"]
        else R + value.summary["RECOMMENDATION"] + N
        if "SELL" in value.summary["RECOMMENDATION"]
        else G + "~~" + N
        if "NEUTRAL" in value.summary["RECOMMENDATION"]
        else value.summary["RECOMMENDATION"]  # Default case, no color
        for key, value in analysis.items()
    ]
    table.add_column(timeframe, column_data)


print(table)
