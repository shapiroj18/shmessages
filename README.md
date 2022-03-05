# Shmessages

## Descriptions
Shell messenger for iMessages and Texts on your Mac.

## Dependencies
**Required**
1. [Python3](https://www.python.org/downloads/macos/)

**Optional**
1. [Sqlite CLI](https://formulae.brew.sh/formula/sqlite) for poking around Apple's databases

## Running Program
1. `cd` to root of this project
2. Start a virtual environment - `Python3 -m venv venv`
3. Activate virtual environment - `. venv/bin/activate`
4. Install dependencies - `pip install -r requirements.txt`

## How it Works
This pulls data from sqlite database files. The main ones are for messages data `chat.db`, found under `~/Library/Messages/chat.db` and contacts data `AddressBook-v22.abcddb`, found under `~/Library/Application Support/AddressBook/Sources/<some folder>/AddressBook-v22.abcddb`. Note that the `.abcddb` extension just resolves to a sqlite database.

## To-Do:
1. Figure out how to handle group messages