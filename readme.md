# маленький REST API сервис для вступительного задания в ШБР

![](https://sun9-81.userapi.com/impg/4xuS9-m_1SNYLeytCs9mCtIsSrCT49MxGh9JoQ/SC2X-4z2oc8.jpg?size=1600x1200&quality=95&sign=42de96cf520b21fc26c55295eb279b08&type=album)

### Функционал

-  ручка /nodes/{id} позволяет по id получить информацию об объекте в файловой системе в формате json
- ручка /imports позволяет добавить объект в файловую систему (информацию следует передовать в формате json)
- ручка /delete/{id} позволяет удалить информацию из файловой системы




**Как развернуть**

	git clone https://github.com/defuntitled/BackendSchoolIntroProject
	cd BackendSchoolIntroProject
	docker-compose up

**Список используемых технологий**
- Flask для разрвботки логики сервиса
- Сервер Gunicorn + Nginx
- Sqlalchemy + sqlite для хранения данных
- Docker