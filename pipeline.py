import pandas as pd


def extract():

    activity = pd.read_csv("activity.csv")
    devices = pd.read_csv("devices.csv")
    users = pd.read_csv("users.csv")

    return activity, devices, users


def transform(activity, devices, users):

    # clean
    activity = activity.dropna(
        subset=["user", "action"]
    ).copy()

    # convert time
    activity["time"] = pd.to_datetime(
        activity["time"],
        errors="coerce"
    )

    # remove invalid time
    activity = activity.dropna(subset=["time"])

    # joins
    df = (
        activity.merge(devices, on="user", how="inner")
                .merge(users, on="user", how="left")
    )

    # aggregations

    top_countries = (
        df.groupby("country")["action"]
        .count()
        .reset_index(name="num_actions")
    )

    most_active = top_countries.loc[
        top_countries["num_actions"].idxmax()
    ]

    most_used = (
        df.groupby("device")["action"]
        .count()
        .reset_index(name="num_actions")
    )

    country_and_devices = (
        df.groupby(["country", "device"])["action"]
        .count()
        .reset_index(name="num_actions")
    )

    return (
        top_countries,
        most_active,
        most_used,
        country_and_devices
    )


def load(
    top_countries,
    most_active,
    most_used,
    country_and_devices
):

    top_countries.to_csv(
        "output/top_countries.csv",
        index=False
    )

    most_used.to_csv(
        "output/most_used_devices.csv",
        index=False
    )

    country_and_devices.to_csv(
        "output/country_device_activity.csv",
        index=False
    )

    print(most_active)


def run_pipeline():

    activity, devices, users = extract()

    (
        top_countries,
        most_active,
        most_used,
        country_and_devices
    ) = transform(activity, devices, users)

    load(
        top_countries,
        most_active,
        most_used,
        country_and_devices
    )


if __name__ == "__main__":
    run_pipeline()
