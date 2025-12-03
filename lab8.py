
# 1
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
unique_ips = set(ips)
print("Unique IP:", unique_ips)

# 2

blocked = {"root", "admin", "test"}
blocked.add("hacker")
blocked.remove("test")
print("new:", blocked)

# 3

blocked_ports = {21, 22, 23, 25}
port = 22

if port in blocked_ports:
    print("Порт запрещён")
else:
    print("Порт разрешён")


# 4

known = {"mal.com", "bad.net"}
new = {"bad.net", "xevil.org"}

not_in_db = new.difference(known)
print("not in:", not_in_db)

# 5

white = {"alice", "bob", "root"}
black = {"root", "admin"}

conflict = white.intersection(black)
print("in both:", conflict)


# 6

system_a = {"CVE-1", "CVE-2"}
system_b = {"CVE-2", "CVE-3"}

all_vulns = system_a.union(system_b)
print("Union:" , all_vulns)


# 7

admin_rights = {"read", "write", "delete"}
user_rights = {"read", "download"}

diff = admin_rights.symmetric_difference(user_rights)
print("Difference:", diff)


# 8

all_passwords = ["123", "qwerty", "test", "123", "qwerty", "admin"]
banned = {"test"}

unique_passwords = set(all_passwords)
clean_passwords = unique_passwords.difference(banned)
print("useful:", clean_passwords)


# 9

global_ips = {"10.0.0.1", "10.0.0.2", "192.168.1.1"}
local_ips = {"10.0.0.2", "10.0.0.3"}

local_ips.intersection_update(global_ips)
print("in:", local_ips)


# 10

logs = ["scan", "debug_mode", "scan", "connect", "debuginfo"]

unique_cmds = set(logs)
result = {cmd for cmd in unique_cmds if "debug" not in cmd}
print("no debug:", result)





# 1.
#Множества: неупорядочены, нет индексов, нет дубликатов, элементы неизменяемые.
#Списки: упорядочены, есть индексы, могут содержать дубликаты.

# 2.
# Нельзя. Они изменяемые (не hashable), а множество хранит только неизменяемые объекты.

# 3.
# remove(x) - удаляет, но если x нет  ошибка.
# discard(x) - удаляет, но если x нет  ничего не происходит.

# 4.
# Оба объединяют множества.
# union() может принимать несколько множеств сразу.

# 5.
# Симметрическая разность - элементы, которые есть в A или B, но не в обоих.

# 6.
# Модифицирует текущее множество, оставляя только пересечение. Ничего не возвращает.

# 7.
# Модифицируют: add, remove, discard, update, intersection_update, difference_update, symmetric_difference_update, clear.
# Возвращают новое: union, intersection, difference, symmetric_difference, copy.