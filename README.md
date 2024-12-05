# How to run
1. get docker
2. cd into project folder
3. set .env file according to example
4. run `flask db init; flask db migrate; flask db upgrade` whith passed env variables (define them in any way)
4. in `docker-compose.yml` set `.env.example` to `.env`
3. run container (`POSTGRES_PASSWORD=<password to your db> docker-compose up`)

# Student info
Дячок Максим Андрійлвич, ІМ-21

## Notes
[Deployed site](https://backend-4-0i8c.onrender.com)

[Flow](https://www.postman.com/test-task-solidgate/workspace/pub-repo/flow/6751775b04060300322d69a0)

[Collection with requests](https://www.postman.com/test-task-solidgate/workspace/pub-repo/collection/30950089-fc578053-4694-45d3-a20a-4151b3fdf1ed?action=share&creator=30950089&active-environment=30950089-2e859448-0f3c-47d0-848b-630b7cb8905b)
