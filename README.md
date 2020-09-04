# Password Manager Server Backend
Backend handler for the password manager project

## Writing `config.yml`
The `config.yml` has the following schema:

```
dbfile: "/absolute/path/to/your/db_file.db"
password: "secret_password"
```

It is expected that the `config.yml` resides in the same directory as where
you're calling `pwmgr.db`.