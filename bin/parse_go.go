package main

import (
	"fmt"
	"path/filepath"
	"path"
	"os"
	"sort"
	"strings"
	"io/ioutil"
	"regexp"
)

const delim = "~"
var structs map[string]*Struct

type Struct struct {
	name string
	fields []string
	methods []string
}

func NewStruct(name string) *Struct {
	s := new(Struct)
	s.name = name
	s.fields = make([]string,0)
	s.methods = make([]string,0)
	return s
}

func (s Struct) Repr() string {
	method_text := "\n\tmethod : "
	methods := ""
	for _, method := range s.methods {
		methods += method_text + method
	}
	field_text := "\n\tfield : "
	fields := ""
	for _, field := range s.fields {
		fields += field_text + field
	}
	repr := fmt.Sprintf("%s :%s%s",s.name,methods,fields)
	return repr
}

func format_line(line string) []string {
	line = strings.Trim(line, " \t")
	re := regexp.MustCompile(" +")
	line = re.ReplaceAllString(line," ")
	re = regexp.MustCompile(`([,{\(\[}\)\]])`)
	line = re.ReplaceAllString(line,delim+`$1`+delim)
	re = regexp.MustCompile(" ")
	line = re.ReplaceAllString(line,delim)
	re = regexp.MustCompile(delim+"+")
	line = re.ReplaceAllString(line,delim)
	line = strings.Trim(line, delim)
	return strings.Split(line,delim)
}

func add_func(line []string) {
	if line[1] == "(" {
		name := strings.Trim(line[3],"*")
		if _, exists := structs[name]; !exists {
			structs[name] = NewStruct(name)
		}
		structs[name].methods = append(structs[name].methods,line[5])
	}
}

func add_type(line []string) {
	name := line[1]
	if _, exists := structs[name]; !exists {
		structs[name] = NewStruct(name)
	}
	if line[2] != "struct" && line[2] != "interface" {
		var typename string
		if line[len(line)-3] != "interface" {
			typename = line[len(line)-1]
		} else {
			typename = line[len(line)-3]
		}
		structs[name].fields = append(structs[name].fields,strings.Trim(typename,"*"))
	}
}

func add_field(line []string, name string) {
	if _, exists := structs[name]; !exists {
		structs[name] = NewStruct(name)
	}
	if line[1] == "map" {
		structs[name].fields = append(structs[name].fields,strings.Trim(line[5],"*"))
	} else if line[1] == "[" {
		if line[2] == "]" {
			structs[name].fields = append(structs[name].fields,strings.Trim(line[3],"*"))
		} else {
			if line[4] == "[" {
				structs[name].fields = append(structs[name].fields,strings.Trim(line[7],"*"))
			} else {
				structs[name].fields = append(structs[name].fields,strings.Trim(line[4],"*"))
			}
		}
	} else if line[1] == "(" {
		structs[name].fields = append(structs[name].fields,strings.Trim(line[0],"*"))
	} else {
		structs[name].fields = append(structs[name].fields,strings.Trim(line[1],"*"))
	}
}

func main() {
	structs = make(map[string]*Struct)
	filenames, err := filepath.Glob(path.Join(os.Getenv("postprompt"),"src","postprompt","*"))
	if err != nil {
		panic(err)
	}
	for _, filename := range filenames {
		//fmt.Println(filename)
		b, err := ioutil.ReadFile(filename)
		if err != nil {
			panic(err)
		}
		in_struct := false
		in_interface := false
		structname := ""
		ifacename := ""
		for _, raw_line := range strings.Split(string(b),"\n") {
			line := format_line(raw_line)
			//fmt.Println(strings.Join(line,"|"))
			keyword := line[0]
			if keyword == "type" {
				add_type(line)
				if len(line) > 3 && line[2] == "struct" && line[len(line)-1] != "}" {
					in_struct = true
					structname = line[1]
				} else if len(line) > 3 && line[2] == "interface" && line [len(line)-1] != "}" {
					in_interface = true
					ifacename = line[1]
				}
			} else if keyword == "func" {
				add_func(line)
			} else if in_struct {
				if line[0] == "}" {
					in_struct = false
				} else {
					add_field(line,structname)
				}
			} else if in_interface {
				if line[0] == "}" {
					in_interface = false
				} else {
					add_field(line,ifacename)
				}
			}
		}
	}
	keys := make([]string,len(structs))
	i := 0
	for key, _ := range structs {
		keys[i] = key
		i++
	}
	sort.Strings(keys)
	for _, key := range keys {
		fmt.Println(structs[key].Repr())
	}
}
