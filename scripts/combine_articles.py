import os
import glob

def combine_blog_articles():
    """
    Собирает все статьи из content/blog в один md файл.
    """
    blog_dir = 'content/blog'
    output_file = 'all_articles.md'
    
    # Находим все md файлы, кроме _index.md
    files_to_process = [f for f in glob.glob(os.path.join(blog_dir, '*.md')) if not f.endswith('_index.md')]
    
    # Сортируем файлы, чтобы порядок был предсказуемым (например, по имени)
    files_to_process.sort()
    
    all_content = []
    
    for filepath in files_to_process:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

            parts = content.split('---', 2)

            if len(parts) < 3:
                continue
            
            front_matter = parts[1]
            article_body = parts[2]
            title = "Без названия"
            for line in front_matter.strip().split('\n'):
                if line.strip().startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"\'')
                    break

            all_content.append(f"# {title}\n\n")
            
            all_content.append(article_body.lstrip())
            all_content.append("\n\n---\n\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(all_content)
        
    print(f"Все статьи успешно собраны в файл: {output_file}")

if __name__ == '__main__':
    combine_blog_articles()