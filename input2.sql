IF not exists (select * from sysobjects where name='TRACKING' and xtype='U')

BEGIN

CREATE TABLE dbo.TRACKING (
    TRACKING_KEY INT NOT NULL,
    C_KEY INT NULL,
    USER_KEY INT NULL,
    ACTION_DATETIME DATE NULL,
    SOURCE NVARCHAR(20) NULL,
    [ACTION] NVARCHAR(20) NULL,
    [DESC] NVARCHAR(100) NULL,
    CONSTRAINT PK_TRACKING
        PRIMARY KEY CLUSTERED (TRACKING_KEY)
)

INSERT INTO TRACKING (
        [TRACKING_KEY],
        [C_KEY],
        [USER_KEY],
        [ACTION_DATETIME],
        [SOURCE],
        [ACTION],
        [DESC]
    )
    VALUES (
        -1,
        -1
    )

END
GO

