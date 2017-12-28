#!/bin/bash

if [ ! -f /src/db/cards.db ]; then
	cp cards-empty.db /src/db/cards.db
fi

gunicorn --bind  0.0.0.0:8000 flash_cards:app