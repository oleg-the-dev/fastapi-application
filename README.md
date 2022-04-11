# FastAPI application

Simple API for warehouse with users, items, role system and JWT-token based authentication. Covered with pytest.

![demo](https://sun9-80.userapi.com/impf/sBcI2693IlfE7P-e5vTIY4GXgBG_gTSXAZxmIA/CeFdehqeIEg.jpg?size=1421x367&quality=96&sign=f1b2170c89dc0153e09248b0ea27c184&type=album)


# How to use it
1. Clone repository.
2. Install requirements: `pip3 install -r requirements.txt`
3. **Run init_db.py in app.database folder**. It will create two separate databases in root directory (*dev.db* and *test.db*) and inject some basic data.
4. Run `uvicorn main:app` in terminal to start the server.
5. If you want to run tests just run `pytest` in terminal.
