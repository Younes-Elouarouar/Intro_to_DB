SELECT 
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_DEFAULT AS 'Default Value',
    CHARACTER_MAXIMUM_LENGTH AS 'Max Length',
    NUMERIC_PRECISION AS 'Numeric Precision',
    NUMERIC_SCALE AS 'Numeric Scale',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra Information'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE() -- Current database
    AND TABLE_NAME = 'books';
