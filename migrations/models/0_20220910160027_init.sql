-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "username" VARCHAR(100) NOT NULL UNIQUE,
    "firstname" VARCHAR(100) NOT NULL,
    "lastname" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "password" VARCHAR(256) NOT NULL,
    "verified" INT NOT NULL  DEFAULT 0,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "business" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "name" VARCHAR(256) NOT NULL UNIQUE,
    "city" VARCHAR(100) NOT NULL,
    "region" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "logo" VARCHAR(256),
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "admin_id" CHAR(36) NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "product" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "category" VARCHAR(200) NOT NULL,
    "original_price" VARCHAR(40) NOT NULL,
    "new_price" VARCHAR(40) NOT NULL,
    "percentage_discount" INT NOT NULL  DEFAULT 0,
    "offer_expiration" DATE NOT NULL,
    "image" VARCHAR(256),
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "business_id" CHAR(36) NOT NULL REFERENCES "business" ("id") ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS "idx_product_name_683352" ON "product" ("name");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
