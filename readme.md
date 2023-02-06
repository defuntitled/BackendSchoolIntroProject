# маленький REST API сервис для вступительного задания в ШБР


### Функционал

-  ручка /nodes/{id} позволяет по id получить информацию об объекте в файловой системе в формате json
- ручка /imports позволяет добавить объект в файловую систему (информацию следует передовать в формате json)
- ручка /delete/{id} позволяет удалить информацию из файловой системы




**Как развернуть**

	git clone https://github.com/defuntitled/BackendSchoolIntroProject
	cd BackendSchoolIntroProject
	docker-compose up

**Список используемых технологий**
- Flask для разработки логики сервиса
- Сервер Gunicorn + Nginx
- Sqlalchemy + sqlite для хранения данных
- Docker
