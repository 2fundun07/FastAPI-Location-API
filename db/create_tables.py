import database as db


def main():
    print("creating tables...")
    db.Base.metadata.create_all(bind=db.engine)


if __name__ == "__main__":
    main()
