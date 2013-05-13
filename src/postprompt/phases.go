package postprompt

type Phase int
type SuperPhase int

const (
	DrawPhase Phase = iota
	PrePhase
	MainPhase
	EndPhase
	StepOnePhase = 1
)

const (
	PreSuperPhase SuperPhase = iota
	MainSuperPhase
	DoneSuperPhase
	StepOneSuperPhase = 1
)

