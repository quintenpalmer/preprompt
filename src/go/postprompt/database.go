package postprompt

import (
	"fmt"
    "database/sql"
    _ "github.com/ziutek/mymysql/godrv"

)

type ppdatabase struct {
	con *sql.DB
}

func NewDatabase(database,user,password string) *ppdatabase {
	db := new(ppdatabase)
	con, err := sql.Open("mymysql",database+"/"+user+"/"+password)
	if err != nil {
		fmt.Println("DB ERROR")
	}
	db.con = con
	//defer db.con.Close()
	return db
}

func SelectRows(db *ppdatabase, command string) {
	rows, err := db.con.Query(command)
	if err != nil {
		fmt.Println("DB ERROR")
	}
	var id int
	var name, effect string
	for rows.Next() {
		if rows.Scan(&id,&name,&effect) != nil {
			fmt.Println("DB ERROR")
		}
		fmt.Println(id,name,effect)
	}
}
