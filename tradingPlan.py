from tradingview_ta import Interval, get_multiple_analysis
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
    # add the exchange to all the symbols
    # symbols (list): List of EXCHANGE:SYMBOL (ex: ["NASDAQ:AAPL"] or ["BINANCE:BTCUSDT"] or ["FX_IDC:USDCAD"])
    symbols = [f"FX_IDC:{symbol}" for symbol in WATCH_LIST]
    
    analysis = {}

    for time in TIME_FRAMES:
        match time:
            case "M1":
                analysis["M1"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_1_MONTH,
                    symbols=symbols)
            case "W1":
                analysis["W1"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_1_WEEK,
                    symbols=symbols)
            case "D1":
                analysis["D1"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_1_DAY,
                    symbols=symbols)
            case "H4":
                analysis["H4"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_4_HOURS,
                    symbols=symbols)
            case "H2":
                analysis["H2"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_2_HOURS,
                    symbols=symbols)
            case "H1":
                analysis["H1"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_1_HOUR,
                    symbols=symbols)
            case "M30":
                analysis["M30"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_30_MINUTES,
                    symbols=symbols)
            case "M15":
                analysis["M15"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_15_MINUTES,
                    symbols=symbols)
            case "M5":
                analysis["M5"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_5_MINUTES,
                    symbols=symbols)
            case "M1":
                analysis["M1"] = get_multiple_analysis(
                    screener="forex",
                    interval=Interval.INTERVAL_1_MINUTE,
                    symbols=symbols)
            case _:
                raise Exception("Invalid Time Frame")

    return analysis

def print_table(all_analysis_data):
    # Color
    R = "\033[0;31;40m"  # RED
    G = "\033[90m"  # Grey for Neutral
    Y = "\033[0;33;40m"  # Yellow
    B = "\033[0;34;40m"  # Blue
    N = "\033[0m"  # Reset
    
    table = PrettyTable()
    table.add_column("", WATCH_LIST)

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

if __name__ == "__main__":
    all_analysis_data = get_analysis_for_multiple_timeframes()
    print_table(all_analysis_data)
