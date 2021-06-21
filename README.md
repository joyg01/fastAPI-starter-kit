pip install .\extras\opentoken-python-master.zip

## FastAPI starter kit

- FastAPI
- Pytest
- Dockerfile
- OpenToken decode (custom for pfizer SSO)
- User routes with authorization
- Admin routes with authorization



#### Usage
```
pip install -r requirements
pip install .\extras\opentoken-python-master.zip
```
Set ENV variables
```
$Env:OPEN_TOKEN_NAME = "opentokenApacheDedicated"
$Env:OPEN_TOKEN_PASSWORD = ""
$Env:ADMIN_GROUP = "group_for_admins"
$Env:USER_GROUP = "group_for_users"
```
Run Fast API
```
 uvicorn main:app --host 0.0.0.0 --port 5678
```
Run Pytest
```
pytest
```
Build Docker image
```
docker build -t fastapi .

docker run -t -d --name mycontainer12 -p 5679:5678  -e OPEN_TOKEN_PASSWORD="" -e OPEN_TOKEN_NAME="" -e ADMIN_GROUP="" -e USER_GROUP="" fastapi
```