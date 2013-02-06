from control.load.lstructs import Direct_Damage,Do_Nothing,Valid_Activate,In_Valid_persist,Add_Damage,Valid_Trigger_Cond,On_Damager,Do_Nothing_Trigger,Timed_Persist
from model.card_effect.instant import Instant_List, Instant
from model.card_effect.persist import Persist_Cond_list
from model.card_effect.persist_activate import Persist_Activate_list,Persist_Activate
from model.card_effect.effect import Effect
from model.control_state import phase
from pyplib.errors import PP_Game_Action_Error
from model.card import Card

def get_direct_damage(elemental,amount):
	instants = Instant_List(instants=[Instant(effect=Direct_Damage(elemental=elemental,amount=amount),conds=[Valid_Activate()])],valid_phase=phase.main)
	persists = Persist_Cond_list(does_persist=False,conds=[In_Valid_persist()])
	pactivates = Persist_Activate_list(pactivates=[Persist_Activate(effect=Do_Nothing_Trigger(),conds=[Valid_Trigger_Cond()])])
	return Effect(instants=instants,persists=persists,pactivates=pactivates,elemental=elemental)

def get_sits_n_turns(elemental,duration):
	instants = Instant_List(instants=[Instant(effect=Do_Nothing(),conds=[Valid_Activate()])],valid_phase=phase.main)
	persists = Persist_Cond_list(does_persist=True,conds=[Timed_Persist(duration=duration)])
	pactivates = Persist_Activate_list(pactivates=[Persist_Activate(effect=Do_Nothing_Trigger(),conds=[Valid_Trigger_Cond()])])
	return Effect(instants=instants,persists=persists,pactivates=pactivates,elemental=elemental)

def alters_m_sits_n_turns(elemental,args):
	tmp = args.split('/')
	duration = int(tmp[0])
	amount = int(tmp[1])
	who = [int(t) for t in tmp[2]]
	instants = Instant_List(instants=[Instant(effect=Do_Nothing(),conds=[Valid_Activate()])],valid_phase=phase.main)
	persists = Persist_Cond_list(does_persist=True,conds=[Timed_Persist(duration=duration)])
	pactivates = Persist_Activate_list(pactivates=[Persist_Activate(effect=Add_Damage(elemental=elemental,amount=amount),conds=[On_Damager(who=who)])])
	return Effect(instants=instants,persists=persists,pactivates=pactivates,elemental=elemental)

def lookup_table(lookup_string):
	tmp = lookup_string.split('-')
	elemental_type = tmp[0]
	effect_type = tmp[1]
	params = tmp[2]
	return Card(name=tmp[1],effect=get_effect_from_name(effect_type)(elemental_type,params))


# name to effect mapping
ntoe = {}
ntoe['damage'] = get_direct_damage
ntoe['persists'] = get_sits_n_turns
ntoe['alter'] = alters_m_sits_n_turns
def get_effect_from_name(name):
	try:
		return ntoe[name]
	except KeyError:
		raise PP_Game_Action_Error("Could not load effect name %s"%str(name))
