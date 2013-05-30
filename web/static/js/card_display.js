/* Displays the small version of a card.
Right now this only displays a single static card; eventually it should get
information from the database and build the appropriate card based on input. */
function display_icon(id, action, name) {
	var card = document.createElement("div");
		card.setAttribute("class", "click-overlay");
		if (action != null) { // apply the action, if there is one
			card.onclick = function(){ action(event) };
		}
		card.setAttribute("id", id);
	var rarity = document.createElement("div");
		rarity.setAttribute("class", "card-rarity-gold");
	var frame = document.createElement("div");
		frame.setAttribute("class", "card-frame-red");
	var art = document.createElement("div");
		art.setAttribute("class", "card-art");
		art.innerHTML = "<img src=\"/static/images/cards/art/0000i_Test.png\">";
	var desc = document.createElement("div");
		desc.setAttribute("class", "card-desc");
		desc.innerHTML += name; /* one of these lines for each icon */

	frame.appendChild(art); /* top-most */
	frame.appendChild(desc);
	rarity.appendChild(frame);
	rarity.appendChild(card);

	return rarity; /* returns the generated card icon */
}

/* Displays a face-down card. */
function display_back() {
	var card = document.createElement("div");
		card.setAttribute("class", "card-back");
	return card; /* returns the generated card icon */
}
