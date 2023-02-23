import pandas as pd


def clean(contact_info_file,other_info_file):
    contact = pd.read_csv(contact_info_file)
    other = pd.read_csv(other_info_file)
    df = pd.merge(contact, other, left_on="respondent_id", right_on="id", how="outer")
    df = df.drop("id", axis=1)
    df = df.dropna()
    df = df[df["job"].str.contains( "insurance|Insurance" )==False ]
    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("contact_info_file", help='respondent_contact (CSV)')
    parser.add_argument("other_info_file", help='respondent_other (CSV)')
    parser.add_argument('output_file', help='output_file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file,args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)
    respondent_cleaned = pd.read_csv(args.output_file)
    print(respondent_cleaned.shape)