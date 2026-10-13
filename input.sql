IF not exists (select * from sysobjects where name='TRACKING' and xtype='U')



CREATE TABLE dbo.TRACKING (
    TRACKING_KEY INT NOT NULL,
    C_KEY INT NULL

)

INSERT INTO TRACKING (
        [TRACKING_KEY],
        [C_KEY]

    )
    VALUES (
        -1,
        -1
    )

GO