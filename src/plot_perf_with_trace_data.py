import argparse
import os
import pandas as pd
from typing import Tuple

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plot Jaeger trace data for a given service.")
    parser.add_argument("--test-name", type=str, required=True, help="Test name")
    parser.add_argument("--service-name-for-traces", type=str, required=True, help="Service name for traces")
    parser.add_argument("--container-name", type=str, required=True, help="Service name")
    parser.add_argument("--config", type=str, required=True, help="Test configuration")
    parser.add_argument("--data-dir", type=str, required=True, help="Data directory")
    
    return parser.parse_args()

def load_traces_data(
        data_dir: str,
        service_name_for_traces: str,
        test_name: str,
        config: str,
        container_name: str
        ) -> pd.DataFrame:
    jaeger_traces_csv_file_path: str = os.path.join(data_dir, "data", 
                                                    f"{service_name_for_traces}_{test_name}_{config}_traces_data.csv")
    jaeger_traces_df: pd.DataFrame = pd.read_csv(jaeger_traces_csv_file_path)
    container_jaeger_traces_df: pd.DataFrame = jaeger_traces_df[jaeger_traces_df['container_name'] == container_name]
    
    return container_jaeger_traces_df

def load_perf_data(data_dir: str) -> pd.DataFrame:
    llc_data_file: str = f"{data_dir}/data/perf_data.csv"
    df: pd.DataFrame = pd.read_csv(llc_data_file, sep=",")
    df["Time"] = df["Time"] - df["Time"].min()
    return df

def create_trace_request_df(
        container_jaeger_traces_df: pd.DataFrame,
        service_name_for_traces: str
        ) -> pd.DataFrame:
    # group the data frames by trace id ad output a df which has start and end non idle times for a specific servicename
    return pd.DataFrame()

def main() -> None:
    args: argparse.Namespace = parse_arguments()

    test_name: str = args.test_name.replace(" ", "_")
    service_name_for_traces: str = args.service_name_for_traces
    container_name: str = args.container_name
    config: str = args.config.replace(" ", "_")
    data_dir: str = args.data_dir

    print("Plotting Jaeger trace data")
    print(f"Test Name: {test_name}")
    print(f"Service Name for Traces: {service_name_for_traces}")
    print(f"Container Name: {container_name}")
    print(f"Config: {config}")
    print(f"Data Directory: {data_dir}")

    container_jaeger_traces_df: pd.DataFrame = load_traces_data(
        data_dir, service_name_for_traces, test_name, config, container_name)
    perf_df: pd.DataFrame = load_perf_data(data_dir)

    # TODO: complete
    

if __name__ == "__main__":
    main()