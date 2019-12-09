Репозиторий курса PY-111
=

**Как пользоваться данным репозиторием?**

- Сделайте копию данного репозитория, нажав зеленую кнопку ""Use this template наверху страницы
- Добавьте в настройках репозитория в вкладке Collaborators вашего преподавателя по практике
- Создайте новую ветку с любым именем <PRIVATE_BRANCH_NAME> у себя в форке
- Склонируйте репозиторий на ваше устройство

**Выполнение заданий**
Выполнение заданий подразумевается в вашей ветке (**не** ветке master). После завершения задания вам необходимо сделать pull-request себе в master и поставить вашего преподавателя по практике в качестве reviewer'а.

Выполните следующий шаг, чтобы переключиться к вашей личной ветке:

```
git checkout <PRIVATE_BRANCH_NAME>
```

Затем создайте новую ветку для выполнения задания:

```
git checkout -b <TASK_BRANCH>
```

Откройте вашу любимую IDE и напишите код для решения задачи, после чего не забудьте сделать коммит.

```
git add .
git commit -m "cool message"
```

Когда вы сочтете, что ваше задание решено, вы должны слить изменения из ветки с заданием в вашу приватную ветку:

```
git checkout <PRIVATE_BRANCH_NAME>
git merge <TASK_BRANCH>
```

Теперь вы можете отправить ваши изменения в ваш собственный удаленный репозиторий:
 
```
git push origin <PRIVATE_BRANCH_NAME>
```

Когда ваши изменения отправились в ваш собственный репозиторий, вам необходимо сделать пулл-реквест себе в master и поставить преподавателя по практике в качестве reviewer'а (на панели справа при создании pull-request'а).

**Как помочь данному репозиторию**

Вы можете помочь данному репозиторию, создавая или исправляя тесты для заданий. Создайте тест и отправьте пулл-реквест с пометкой "Test", чтобы я обратил на это внимание.

Также, если вы нашли ошибку (в тесте, в документации, в аннотации и т.д.) - можете создать issue и указать, где и что стоит поправить, или поправить и сделать пулл реквест в оригинальный репозиторий.
