# Computer Science Flash Cards

## Convert from .db to .csv

```./sqlite_to_csv cards.db cards.csv```

## Convert from .csv to .db

```./csv_to_sqlite cards.csv cards.db```

## Kill cs-flash-cards Docker process

```./kill.sh```

### Remove cs-flash-cards Docker image

```./rmi.sh```

## Combine .csv files

```cat math.csv system.csv java.csv > interview.csv```

## How to run with Docker

```
./build.sh  # Build local Docker image
./run.sh
```

### Initialize new database

Open localhost/initdb
