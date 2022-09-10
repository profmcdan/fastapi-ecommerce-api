## FASTAPI APP

## Migrations
Initialize aerich for migrations 

```bash
aerich init -t src.configs.db.TORTOISE_ORM
aerich init-db
tree migrations/
```

Subsequently, you can run migrations with 
```bash
aerich migrate --name add_email
aerich upgrade
```

For rollback
```bash
aerich downgrade
```
