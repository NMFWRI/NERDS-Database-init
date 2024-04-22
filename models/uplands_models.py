from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, Double, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

UplandsBase = declarative_base()


class AdminUnit(UplandsBase):
	__tablename__ = 'AdminUnit'

	AdminUnit = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Comment = Column(
		Text
		)
	DateCreated = Column(
		DateTime
		)


class AerialCover(UplandsBase):
	__tablename__ = 'AerialCover'

	Comments = Column(
		Text
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Forbs = Column(
		Double(8)
		)
	Gram = Column(
		Double(8)
		)
	Shrubs = Column(
		Double(8)
		)
	TreeRegen = Column(
		Double(8)
		)


class CanopyDensiometer(UplandsBase):
	__tablename__ = 'CanopyDensiometer'

	Canopy = Column(
		String(255)
		)
	Comment = Column(
		Text
		)
	DensE = Column(
		Integer
		)
	DensN = Column(
		Integer
		)
	DensS = Column(
		Integer
		)
	DensW = Column(
		Integer
		)
	DotsCount = Column(
		Integer
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Point = Column(
		Integer
		)
	Transect = Column(
		Integer
		)


class DamageCodes(UplandsBase):
	__tablename__ = 'DamageCodes'

	DamageCat = Column(
		String(255),
		primary_key=True,
		comment="""USFS Damage Category""",
		nullable=False
		)
	DamageCode = Column(
		String(255),
		primary_key=True,
		comment="""NPS Damage Code""",
		nullable=False
		)
	Description = Column(
		Text,
		comment="""Damage description"""
		)
	Notes = Column(
		Text,
		comment="""Additional notes"""
		)


class DamageSev(UplandsBase):
	__tablename__ = 'DamageSev'

	DamageCode = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	DamageSev = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Description = Column(
		Text
		)
	Notes = Column(
		Text
		)


class Event(UplandsBase):
	__tablename__ = 'Event'

	CameraID = Column(
		String(255)
		)
	Comment = Column(
		Text
		)
	Declination = Column(
		Double(8),
		default=7,
		comment="""Magnetic declination in degrees"""
		)
	EventDate = Column(
		DateTime,
		nullable=False
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	FuelsObserver = Column(
		String(255)
		)
	FuelsRecorder = Column(
		String(255)
		)
	MonitoringStatus = Column(
		String(255)
		)
	Personnel = Column(
		String(255)
		)
	PlotID = Column(
		String(255),
		nullable=False
		)
	PlotObserver = Column(
		String(255)
		)
	PlotRecorder = Column(
		String(255)
		)
	TreeObserver = Column(
		String(255)
		)
	TreeRecorder = Column(
		String(255)
		)
	VisitID = Column(
		String(255)
		)


class Fuels1000Hr(UplandsBase):
	__tablename__ = 'Fuels1000Hr'

	Comment = Column(
		Text
		)
	DecayClass = Column(
		String(255)
		)
	Diameter = Column(
		Double(8)
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	LogNum = Column(
		Integer,
		primary_key=True,
		nullable=False
		)
	Transect = Column(
		Integer,
		primary_key=True,
		nullable=False
		)


class FuelsDuffLitter(UplandsBase):
	__tablename__ = 'FuelsDuffLitter'

	Comment = Column(
		String(255)
		)
	DuffDepth = Column(
		Double(8)
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	FuelbedDepth = Column(
		Double(8)
		)
	LitterDepth = Column(
		Double(8)
		)
	Offset = Column(
		Integer
		)
	SampleLoc = Column(
		Integer,
		primary_key=True,
		nullable=False
		)
	Transect = Column(
		Integer,
		primary_key=True,
		nullable=False
		)


class FuelsFine(UplandsBase):
	__tablename__ = 'FuelsFine'

	Comment = Column(
		Text
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	HundredHour = Column(
		Integer
		)
	OneHour = Column(
		Integer
		)
	Slope = Column(
		Integer
		)
	TenHour = Column(
		Integer
		)
	Transect = Column(
		Integer,
		primary_key=True,
		nullable=False
		)


class FuelsVegetation(UplandsBase):
	__tablename__ = 'FuelsVegetation'

	Comment = Column(
		Text
		)
	Cover = Column(
		Double(8)
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Height = Column(
		Double(8)
		)
	Item = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Offset = Column(
		Integer
		)
	SampleLoc = Column(
		Integer,
		primary_key=True,
		nullable=False
		)
	Transect = Column(
		Integer,
		primary_key=True,
		nullable=False
		)


class GroundCover(UplandsBase):
	__tablename__ = 'GroundCover'

	BareSoil = Column(
		Double(8)
		)
	Bole = Column(
		Double(8)
		)
	Comment = Column(
		Text
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Gravel = Column(
		Double(8)
		)
	Litter = Column(
		Double(8)
		)
	PlantBasal = Column(
		Double(8)
		)
	Rock = Column(
		Double(8)
		)


class PhotoLog(UplandsBase):
	__tablename__ = 'PhotoLog'

	BackDesc = Column(
		Text,
		comment="""Background descriptors"""
		)
	Comment = Column(
		Text,
		comment="""Additional comments"""
		)
	Crew = Column(
		String(255),
		comment="""Crew intials of who took the photos"""
		)
	DateTime = Column(
		DateTime,
		comment="""Date the photo was taken"""
		)
	Direction = Column(
		String(255),
		comment="""Direction facing when the photo was taken"""
		)
	Distance = Column(
		Double(8),
		default=0,
		comment="""Distance from photo target (default in feet)"""
		)
	DistanceUnits = Column(
		String(255),
		default="""Feet""",
		comment="""Default units for distance"""
		)
	EventID = Column(
		String(255),
		comment="""Event ID""",
		nullable=False
		)
	ForeDesc = Column(
		Text,
		comment="""Foreground descriptors"""
		)
	Lat = Column(
		Double(8),
		comment="""Latitude of photo location (dd.ddd)"""
		)
	Long = Column(
		Double(8),
		comment="""Longitude of the photo location (ddd.ddd)"""
		)
	PhotoID = Column(
		String(255),
		primary_key=True,
		comment="""ID of the photo""",
		nullable=False
		)
	PhotoNum = Column(
		String(255),
		comment="""Photo ID produced by the camera"""
		)


class Plot(UplandsBase):
	__tablename__ = 'Plot'

	AdminUnit = Column(
		String(255)
		)
	Aspect = Column(
		Integer
		)
	Azimuth = Column(
		Integer
		)
	Comment = Column(
		Text
		)
	Datum = Column(
		String(255)
		)
	Elevation = Column(
		Double(8)
		)
	LatDD = Column(
		Double(8)
		)
	LongDD = Column(
		Double(8)
		)
	PlotID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	PlotName = Column(
		String(255)
		)
	PlotType = Column(
		String(255)
		)
	Slope = Column(
		Integer
		)
	UtmX = Column(
		String(255)
		)
	UtmY = Column(
		String(255)
		)


class Project(UplandsBase):
	__tablename__ = 'Project'

	AdminUnit = Column(
		String(255)
		)
	Agency = Column(
		String(255)
		)
	Area = Column(
		Double(8)
		)
	Comment = Column(
		Text
		)
	DateCreated = Column(
		DateTime,
		nullable=False
		)
	Description = Column(
		Text
		)
	Objective = Column(
		Text
		)
	ProjectID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	ProjectName = Column(
		String(255)
		)


class ProjectDetail(UplandsBase):
	__tablename__ = 'ProjectDetail'

	Acres = Column(
		Double(8)
		)
	BreakDiam = Column(
		Double(8)
		)
	Comment = Column(
		Text
		)
	Crew = Column(
		String(255)
		)
	LongTerm = Column(
		Boolean
		)
	NumBrowns = Column(
		Integer
		)
	PlotSize = Column(
		Double(8)
		)
	Project = Column(
		String(255)
		)
	ProjectID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	ProposalID = Column(
		String(255)
		)
	TxClass = Column(
		String(255)
		)
	TxDates = Column(
		String(255)
		)


class ProjectVisit(UplandsBase):
	__tablename__ = 'ProjectVisit'

	MonitoringStatus = Column(
		String(255)
		)
	ProjectID = Column(
		String(255)
		)
	VisitID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	VisitNotes = Column(
		Text
		)
	VisitOrder = Column(
		Integer
		)
	VisitYear = Column(
		Integer
		)


class Species(UplandsBase):
	__tablename__ = 'Species'

	BaseSymbol = Column(
		String(255),
		comment="""USDA symbol (one:many relationship)"""
		)
	CommonName = Column(
		String(255),
		comment="""State Common Name"""
		)
	Family = Column(
		String(255),
		comment="""Latin family of plant"""
		)
	SciName = Column(
		String(255),
		comment="""Scientific Name with Author"""
		)
	Symbol = Column(
		String(255),
		primary_key=True,
		comment="""Used USDA symbol""",
		nullable=False
		)
	SynSymbol = Column(
		String(255),
		comment="""USDA synonym (used for subspecies and variations)"""
		)


class Transect(UplandsBase):
	__tablename__ = 'Transect'

	Azimuth = Column(
		Integer,
		comment="""Azimuth of transect"""
		)
	EventID = Column(
		String(255),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	Length = Column(
		Integer,
		comment="""Length of transect in feet"""
		)
	Slope = Column(
		Double(8),
		comment="""Slope of transect"""
		)
	TransNum = Column(
		Integer,
		primary_key=True,
		comment="""Transect number for the sample event""",
		nullable=False
		)


class TreesIndv(UplandsBase):
	__tablename__ = 'TreesIndv'

	Age = Column(
		Integer
		)
	Cfbh = Column(
		Double(8)
		)
	CharHeight = Column(
		Double(8)
		)
	Ckr = Column(
		Integer
		)
	Comment = Column(
		Text
		)
	CrownClass = Column(
		String(255)
		)
	CrownRad = Column(
		Double(8)
		)
	CrownRatio = Column(
		String(255)
		)
	CrownScPerc = Column(
		Integer
		)
	DamageCode1 = Column(
		String(255)
		)
	DamageCode2 = Column(
		String(255)
		)
	DamageCode3 = Column(
		String(255)
		)
	DamageCode4 = Column(
		String(255)
		)
	DamageCode5 = Column(
		String(255)
		)
	DamageSev1 = Column(
		String(255)
		)
	DamageSev2 = Column(
		String(255)
		)
	DamageSev3 = Column(
		String(255)
		)
	DamageSev4 = Column(
		String(255)
		)
	DamageSev5 = Column(
		String(255)
		)
	Dbh = Column(
		Double(8)
		)
	DecayClass = Column(
		String(255)
		)
	Drc = Column(
		Double(8)
		)
	EqDiam = Column(
		Double(8)
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	GrowthRate = Column(
		String(255)
		)
	Height = Column(
		Double(8)
		)
	LadderBase = Column(
		Double(8)
		)
	LadderMax = Column(
		Double(8)
		)
	Lcbh = Column(
		Double(8)
		)
	Mort = Column(
		String(255)
		)
	NumDeadStems = Column(
		Integer
		)
	NumLiveStems = Column(
		Integer
		)
	Qtr = Column(
		Integer
		)
	ScorchHeight = Column(
		Double(8)
		)
	Species = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Status = Column(
		String(255)
		)
	StemNum = Column(
		Integer,
		primary_key=True,
		default=0,
		comment="""Number of stems on tree""",
		nullable=False
		)
	SubFrac = Column(
		String(255)
		)
	TagNum = Column(
		Integer,
		primary_key=True,
		nullable=False
		)
	XCoord = Column(
		Double(8)
		)
	YCoord = Column(
		Double(8)
		)


class TreesSaplings(UplandsBase):
	__tablename__ = 'TreesSaplings'

	AverageHeight = Column(
		Double(8)
		)
	AvgCrownRatio = Column(
		Double(8)
		)
	Comment = Column(
		Text
		)
	Count = Column(
		Integer
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	SizeClassDiam = Column(
		Double(8),
		primary_key=True,
		nullable=False
		)
	Species = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Status = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	SubplotFraction = Column(
		Integer
		)


class TreesSeedlings(UplandsBase):
	__tablename__ = 'TreesSeedlings'

	AgeClass = Column(
		String(255)
		)
	AverageDiam = Column(
		Double(8)
		)
	AvgCrownRatio = Column(
		Double(8)
		)
	Comment = Column(
		Text
		)
	Count = Column(
		Integer
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	SizeClassHt = Column(
		Double(8),
		primary_key=True,
		nullable=False
		)
	Species = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Status = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	SubplotFraction = Column(
		Integer
		)


class WitnessTree(UplandsBase):
	__tablename__ = 'WitnessTree'

	AzFromPc = Column(
		Double(8)
		)
	Comment = Column(
		Text
		)
	ConditionNotes = Column(
		String(255)
		)
	Dbh = Column(
		Double(8)
		)
	DistFromPc = Column(
		Double(8)
		)
	EventID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	FlagColor = Column(
		String(255)
		)
	Ht = Column(
		Double(8)
		)
	LiCrBHt = Column(
		Double(8)
		)
	TreeTag = Column(
		Integer,
		primary_key=True,
		nullable=False
		)
	WitCondition = Column(
		String(255)
		)
	WitSpecies = Column(
		String(255)
		)

