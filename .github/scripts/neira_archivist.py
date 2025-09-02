import os
from github import Github

def main():
    # Аутентификация через встроенный GITHUB_TOKEN
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("❌ GITHUB_TOKEN not found!")

    g = Github(token)
    
    # Указываем ваш репозиторий
    repo_name = "SaveMyDreams/Neira"
    repo = g.get_repo(repo_name)

    # Определяем путь к файлу и его содержимое
    file_path = "log.txt"
    commit_message = "Добавлен файл лога от Нейра-Архивариус"
    content = "Это тестовое содержимое файла, созданное через GitHub Actions."

    try:
        # Попытка получить текущее содержимое файла (если он существует)
        contents = repo.get_contents(file_path)
        # Если файл существует, обновляем его
        repo.update_file(contents.path, commit_message, content, contents.sha)
        print(f"✅ Файл '{file_path}' успешно обновлён в репозитории.")
    except Exception as e:
        if e.status == 404:
            # Если файл не найден (ошибка 404), создаём новый
            repo.create_file(file_path, commit_message, content)
            print(f"✅ Файл '{file_path}' успешно создан в репозитории.")
        else:
            # Если другая ошибка - пробрасываем её
            raise e

if __name__ == "__main__":
    main()
