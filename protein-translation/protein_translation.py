from itertools import takewhile
from typing import List


translations = {
	"AUG": "Methionine",
	"UUU": "Phenylalanine",
	"UUC": "Phenylalanine",
	"UUA": "Leucine",
	"UUG": "Leucine",
	"UCU": "Serine",
	"UCC": "Serine",
	"UCA": "Serine",
	"UCG": "Serine",
	"UAU": "Tyrosine",
	"UAC": "Tyrosine",
	"UGU": "Cysteine",
	"UGC": "Cysteine",
	"UGG": "Tryptophan"
}


def proteins(strand: List) -> List:
	return list(takewhile(None.__ne__,
		[translations.get(codon) for codon in [strand[i : i + 3] for i in range(0, len(strand), 3)]]
	))