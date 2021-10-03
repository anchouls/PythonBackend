# PythonBackend

Чтобы запустить тесты, напишите: `python3 -m pytest`

Чтобы заапустить нагрузочные тесты, напишите: `locust -f tests/locustfile.py`

[Отчет нагрузочного тестирования](Отчет%20нагрузочного%20тестирования.pages)

GraphQL:
Чтобы запустить, напишите: `uvicorn main:app --reload`

```{
  me{
    id
    name
    disease
    symptoms{
      id
      name
    }
  }
  myFriend{
    id
    name
    disease
    symptoms{
      id
      name
    }
  }
  myPet{
    id
    name
    disease
    symptoms{
      id
      name
    }
  }
}