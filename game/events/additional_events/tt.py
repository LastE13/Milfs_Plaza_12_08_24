final_line = ""
# Открываем исходный файл для чтения
with open('test_task.rpy', 'r', encoding='utf-8') as infile:
    # Открываем целевой файл для записи
    with open('task.rpy', 'w', encoding='utf-8') as outfile:
        # Построчно читаем исходный файл
        for line in infile:
            final_line += "    "
            if "GG_Normal: " in line:
                final_line += "show GG Normal\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Normal: '):].strip() + '\"\n'
            elif "GG_Passion: " in line:
                final_line += "show GG Passion\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Passion: '):].strip() + '\"\n'
            elif "GG_Skepticism: " in line:
                final_line += "show GG Skepticism\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Skepticism: '):].strip() + '\"\n'
            elif "GG_Think: " in line:
                final_line += "show GG Think\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Think: '):].strip() + '\"\n'
            elif "GG_Smile: " in line:
                final_line += "show GG Smile\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Smile: '):].strip() + '\"\n'
            elif "GG_Surprise: " in line:
                final_line += "show GG Surprise\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Surprise: '):].strip() + '\"\n'
            elif "GG_Chagrin: " in line:
                final_line += "show GG Chagrin\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Chagrin: '):].strip() + '\"\n'
            elif "GG_Embarrassment: " in line:
                final_line += "show GG Embarrassment\n"
                final_line += "    '[gg]' \""
                final_line += line[len('GG_Embarrassment: '):].strip() + '\"\n'


            elif "BookW_Smile: " in line:
                final_line += "show BiblioGirl Smile:\n"
                final_line += "    'Нэнси' \""
                final_line += line[len('BookW_Smile: '):].strip() + '\"\n'
            elif "BookW_Embarrassment: " in line:
                final_line += "show BiblioGirl Embarrassment\n"
                final_line += "    'Нэнси' \""
                final_line += line[len('BookW_Embarrassment: '):].strip() + '\"\n'
            elif "BookW_Normal: " in line:
                final_line += "show BiblioGirl Normal\n"
                final_line += "    'Нэнси' \""
                final_line += line[len('BookW_Normal: '):].strip() + '\"\n'
            elif "BookW_Passion: " in line:
                final_line += "show BiblioGirl Passion\n"
                final_line += "    'Нэнси' \""
                final_line += line[len('BookW_Passion: '):].strip() + '\"\n'



            elif "GG: " in line:
                final_line += "'[gg]' \""
                final_line += line[len('GG: '):].strip() + '\"\n'
            elif "Нэнси: " in line:
                final_line += "'Нэнси' \""
                final_line += line[len('Нэнси: '):].strip() + '\"\n'
            else:
                final_line = line

            # Записываем каждую строку в целевой файл
            outfile.write(final_line)
            final_line = ""