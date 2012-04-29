package host.model.list;

import shared.model.list.CardList;

public class FullCardList extends CardList{

	public FullCardList(int size){
		super(size);
	}

	public Card pop(){
		Card card = this.cards[this.length-1];
		this.cards[this.length]=null;
		this.length--;
		return card;
	}

	public void push(Card card){
		card.setLocation(length);
		this.cards[this.length]=card;
		this.length++;
	}

	public Card remove(int cardNumber){
		int i=0;
		int j=0;
		for(i=0;i<this.length;i++){
			if(this.cards[i].location==cardNumber){
				Card card = this.cards[i];
				this.cards[i]=null;
				this.length--;
				for(j=i;j<this.length;j++){
					this.cards[j]=this.cards[j+1];
				}
				return card;
			}
		}
		return null;
	}
}
