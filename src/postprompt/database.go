package postprompt

import (
	"fmt"
	"strconv"
	"database/sql"
	_ "github.com/ziutek/mymysql/godrv"

)

var ppdb *ppdatabase = newDatabase("pp_shared","developer","jfjfkdkdlslskdkdjfjf")

func GetPlayerName(uid int) (string, error) {
	rows, err := getRows("select username from auth_user where id="+strconv.Itoa(uid))
	if err != nil { return "", err }
	var name string
	for rows.Next() {
		if err := rows.Scan(&name); err != nil {
			return "", err
		}
	}
	return name, nil
}

func GetCardIds(uid, did int) ([]int, error) {
	cardIds := make([]int,0)
	rows, err := getRows("select card_id from play_decks where uid="+strconv.Itoa(uid)+" and deck_id="+strconv.Itoa(did))
	if err != nil { return nil, err }
	var cardId int
	for rows.Next() {
		if err := rows.Scan(&cardId); err != nil { return nil, err }
		cardId, err := getCardIdFromUniqueId(cardId)
		if err != nil { return nil, err }
		cardIds = append(cardIds,cardId)
	}
	return cardIds, nil
}

func getCardIdFromUniqueId(uniqueId int) (int, error) {
	rows, err := getRows("select card_name_id from play_cards where id="+strconv.Itoa(uniqueId))
	if err != nil { return 0, err }
	var cardId int
	for rows.Next() {
		if err := rows.Scan(&cardId); err != nil { return 0, err }
	}
	return cardId, nil
}

func GetCardInfo(cardId int) (string, string, error) {
	rows, err := getRows("select card_name, card_effect from play_card_names where id="+strconv.Itoa(cardId))
	if err != nil { return "", "", err }
	var cardName string
	var cardEffect string
	for rows.Next() {
		if err := rows.Scan(&cardName,&cardEffect); err != nil { return "", "" , err }
	}
	return cardName, cardEffect, nil
}

type ppdatabase struct {
	con *sql.DB
}

func newDatabase(dbname,user,password string) *ppdatabase {
	db := new(ppdatabase)
	con, err := sql.Open("mymysql",dbname+"/"+user+"/"+password)
	if err != nil { fmt.Println("DB ERROR") }
	db.con = con
	//TODO close db eventually?
	//defer db.con.Close()
	return db
}

func getRows(command string) (*sql.Rows, error) {
	rows, err := ppdb.con.Query(command)
	if err != nil {
		return nil, err
	}
	return rows, nil
}
