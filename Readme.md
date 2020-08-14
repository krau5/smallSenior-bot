# Bot for Small Senior

Tasks   
- [X] Create posts
- [ ] Collect stats
- [ ] Filter chat

Stack
- Python(3.8.2)
- Aiogram(2.9.2)
- MongoDB

____
### Install on your server using venv
Firstly, you need install `venv` on your PC
```
sudo apt install -y python3-venv
```
You need create `venv` for isolate library version using on application:
```shell
python3 -m venv env
source env/bin/activate
deactivate 
```
Install all dependencies
```
pip3 install -r requirements.txt
```
Run the application
```
python -m app
```

### Install using Docker
```
docker-compose up -d
```