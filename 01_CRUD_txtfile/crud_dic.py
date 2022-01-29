import os

path = ".\lib\data" # path location
str_sep = ";.;" # chosen separator

def create_dic():
    with open(path, "r") as file:
        i = 0
        dic = {}
        for line in file.readlines():
            data = line.rstrip().split(str_sep)
            dic[int(data[0])] = data[1:4]
    # print(dic[0][2]) # prints 'yo', third value of first line.
    # print(type(dic[3][1]))
    return dic, int(data[0])

def read_from_dic(dic):
    # [print(f"{k}: {v}") for k, v in dic.items()]
    if (bool(dic)):
        print(" id            nome                       cpf                      cargo           ")
        print("---- ------------------------- ------------------------- ------------------------- ")
        for k, v in dic.items():
            print(f"{k:^4} ", end=" ")
            [print(f"{_:^24} ", end=" ") for _ in v]
            print()
        print("---- ------------------------- ------------------------- ------------------------- ")
    else:
        print("Não há dados cadastrados no banco")

def create(dic, l_id):
    print("--- Cadastro de novo Funcionario ---")
    name = input(">>>Nome: ")
    cpf = input(">>>Cpf: ")
    cargo = input(">>>Cargo: ")
    dic[l_id+1] = [name, cpf, cargo]
    print("------------------------------------")
    return dic, l_id+1

def update(dic):
    read_from_dic(dic)
    try:
        up_key = int(input("Qual cadastro deseja fazer o update? "))
        print("Pressione enter para alterar o proximo dado")
        for i in range(3):
            print("Dado atual: ", dic[up_key][i])
            new_value = input(">>>novo dado: ")
            if len(new_value) > 0:  # JEITO PYTHON É NOT !!!
                dic[up_key][i] = new_value
    except KeyError:
        print("Insira um integer referente a um id existente!")
    except ValueError:
        print("insira um integer!")
    except:
        print("Um erro inesperado aconteceu")
    print("--------------------------------------")
    return dic

def delete(dic):
    read_from_dic(dic)
    try:
        del_key = int(input("Qual id quer deletar? "))
    except ValueError:
        print("Insira um integer!")
    except:
        print("aconteceu um erro inesperado!")
    else:
        try:
            dic.pop(del_key)
            print("O cadastro foi deletado com sucesso!")
        except KeyError:
            print("Insira um integer referente a um id existente!")
        except:
            print("aconteceu um erro inesperado!")
    finally:
        print("--------------------------------------")
        return dic

def delete_all(dic):
    print("--------------------------------------")
    print("Deseja mesmo apagar TODO o banco de dados? (y/n)")
    escolha = input(">>> ")
    if (escolha == 'y'):
        dic.clear()
    print("--------------------------------------")
    return dic

def save_db(dic):
    if (bool(dic)):
        with open(path, 'w') as file:
            for k, v in dic.items():
                data1, data2, data3 = v
                string = str(k)+str_sep+data1+str_sep+data2+str_sep+data3+'\n'
                file.write(string)
    else:
        with open(path, 'w') as file:
            file.write("")

def menu():
    print("""+-------+------------+
| opcao |    menu    |
+-------+------------+
| c     | create     |
| r     | read       |
| u     | update     |
| d     | delete     |
| d_all | delete all |
+-------+------------+""")

menuing = {
    "c": create,
    "r": read_from_dic,
    "u": update,
    "d": delete,
    "d_all": delete_all,
    "m": menu,
}

if (os.path.exists(path) and os.stat(path).st_size > 9):  # 3 separators are 9 bytes.
    db, last_id = create_dic()
else:
    print("Criando um novo database...")
    db, last_id = {}, -1
    with open(path, 'w') as f:
        f.write("")

menu()

while (escolha := input(">>>crud option: ").lower()) in menuing:
    if (escolha == 'c'):
        dic, last_id = menuing.get(escolha)(db, last_id)
    elif (escolha == 'r'):
        menuing.get(escolha)(db)
    elif(escolha == 'm'):
        menuing.get(escolha)()
    else:
        dic = menuing.get(escolha)(db)
    print("> 'm' para ver o menu")
else:
    escolha = input("Quer salvar as alterações?(y/n) ").lower()
    if (escolha == 'y'):
        print("salvando banco de dados...")
        save_db(db)

print("  -Byeee.")