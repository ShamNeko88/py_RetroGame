-- ユーザテーブル
CREATE TABLE test_users(
    id           smallserial   NOT NULL,
    user_name    VARCHAR(20)   NOT NULL,
    password     VARCHAR(10)   NOT NULL,
    admin_flg    CHAR(1)       NOT NULL,
    memo         VARCHAR(100),
    PRIMARY KEY (id),
    UNIQUE(user_name)
);

-- 管理者
INSERT INTO 
    test_users(
        user_name,
        password,
        admin_flg,
        memo
    )
VALUES(
    'admin',
    'admin',
    '1',
    '管理者'
);
