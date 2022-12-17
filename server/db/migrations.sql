-- ale: create prompts tb
CREATE TABLE IF NOT EXISTS prompts (
    "id" VARCHAR(255) PRIMARY KEY,
    "query" TEXT NOT NULL,
    "createdAt" BIGINT NOT NULL
);


-- ale: create responses tb
CREATE TABLE IF NOT EXISTS responses (
  "id" VARCHAR(255) PRIMARY KEY,
  "promptId" VARCHAR(255) NOT NULL,
  "content" TEXT NOT NULL,
  "sentiment" VARCHAR(10) NOT NULL,
  "createdAt" BIGINT NOT NULL
);


