# SQL injections

simplesql = "123 OR 1=1"
dangersql = "123'; DROP TABLE items; --"

# XSS (Cross-Site Scripting)

xss = "<script>alert(1)</script>"

# Path Traversal (Traversal атаки)

path_traversal = "../../etc/passwd"

# Command Injection

command_injection = "123;ls"

#Отправка JSON с инъекцией

json_injection = {
    "id": "123 OR 1=1",
    "name": "'; DROP TABLE items; --"
}

