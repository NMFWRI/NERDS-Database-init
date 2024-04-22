from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

RiparianBase = declarative_base()


class AerialCover(RiparianBase):
	__tablename__ = 'AerialCover'

	Cactus = Column(
		Integer,
		default=0
		)
	Comments = Column(
		String(100)
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	Forbs = Column(
		Integer
		)
	Gram = Column(
		Integer
		)
	Nativity = Column(
		String(255)
		)
	Shrubs = Column(
		Integer
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
	TreeRegen = Column(
		Integer
		)


class bempCanopy(RiparianBase):
	__tablename__ = 'bempCanopy'

	Cover = Column(
		Integer
		)
	EventID = Column(
		String(50),
		primary_key=True
		)
	Height = Column(
		Integer
		)
	Location = Column(
		String(2),
		nullable=False
		)
	Plants = Column(
		Integer
		)


class bempCenterTrees(RiparianBase):
	__tablename__ = 'bempCenterTrees'

	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	LargeCount = Column(
		Integer,
		default=0,
		comment="""Count of >8" DBH/DRC"""
		)
	MedCount = Column(
		Integer,
		default=0,
		comment="""Count of 4-8" DBH/DRC"""
		)
	SmallCount = Column(
		Integer,
		default=0,
		comment="""Count of 2-4" DBH/DRC"""
		)
	Species = Column(
		String(255),
		comment="""Tree species"""
		)


class bempIntercept(RiparianBase):
	__tablename__ = 'bempIntercept'

	Cover = Column(
		String(5),
		comment="""Ground cover; bare, leaf litter, large woody debris"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	Position = Column(
		Integer,
		primary_key=True,
		comment="""Position along 98ft point intercept""",
		nullable=False
		)
	VegForm = Column(
		String(5),
		comment="""Grass, sedge, forb, shrub under 20in, none"""
		)


class bempSmallTrees(RiparianBase):
	__tablename__ = 'bempSmallTrees'

	Count = Column(
		Integer,
		default=0,
		comment="""Tally of small trees or shrubs between 0.2 and 2in DBH/DRC"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""EventID""",
		nullable=False
		)
	Location = Column(
		String(255),
		comment="""Locations along the transect"""
		)


class BioPhysical(RiparianBase):
	__tablename__ = 'BioPhysical'

	AspectAzimuth = Column(
		Integer,
		comment="""dominant aspect azimuth"""
		)
	DepthtoGroundWater = Column(
		String(255),
		comment="""distance to ground water in feet"""
		)
	DisttoStream = Column(
		String(255),
		comment="""distance from project boundary to nearest stream in feet"""
		)
	EcologicalSiteType = Column(
		Text,
		comment="""dominant site type based on NRCS WSS"""
		)
	ElevationFt = Column(
		Integer,
		default=0,
		comment="""elevation on site"""
		)
	FireImpactsDetails = Column(
		Text,
		comment="""comments/details about fire impacts"""
		)
	HinkandOhmartClass = Column(
		String(255),
		comment="""dominant H&O classification based on aerial imagery"""
		)
	KnownFireImpacts = Column(
		Boolean,
		default=False,
		comment="""known fire impacts on site"""
		)
	LandUseCurrent = Column(
		String(255),
		comment="""current dominant land use"""
		)
	LandUsePrevious = Column(
		String(255),
		comment="""previous dominant land use"""
		)
	MaxPercentSlope = Column(
		String(255),
		comment="""maximum percent slope recorded on site"""
		)
	PercentSlope = Column(
		String(255),
		comment="""average site percent slope, in ranges: 5, 10, 15, 20, etc."""
		)
	PreTreatmentSiteDisturbance = Column(
		Text,
		comment="""information on disturbances existing on site prior to treatment implementation"""
		)
	PreviousRestorationTx = Column(
		Boolean,
		default=False,
		comment="""has previous restoration treatment occurred on site?"""
		)
	PreviousRestorationTxInfo = Column(
		Text,
		comment="""information about previous restoration treatments"""
		)
	PrjID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	StreamflowonSite = Column(
		Boolean,
		default=False,
		comment="""is there streamflow on/through the site?"""
		)
	TamariskBeetle = Column(
		Boolean,
		default=False,
		comment="""is tamarisk beetle on site before treatment?"""
		)
	TechnicalLimitations = Column(
		String(255),
		comment="""what are the primary technical challenges/project limitations existing on site?"""
		)
	TechnicalLimitationsComments = Column(
		String(255),
		comment="""additional information on technical limitations"""
		)


class CanopyDensiometer(RiparianBase):
	__tablename__ = 'CanopyDensiometer'

	Canopy = Column(
		String(15)
		)
	Comment = Column(
		String(100)
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
		String(50),
		primary_key=True,
		nullable=False
		)
	Point = Column(
		Integer
		)
	Transect = Column(
		Integer
		)


class DamageCodes(RiparianBase):
	__tablename__ = 'DamageCodes'

	DamageCode = Column(
		String(255),
		primary_key=True,
		comment="""NPS Damage Code""",
		nullable=False
		)
	Description = Column(
		String(255),
		comment="""Damage description"""
		)
	Notes = Column(
		String(255),
		comment="""Additional notes"""
		)


class DamageSev(RiparianBase):
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


class Event(RiparianBase):
	__tablename__ = 'Event'

	CameraID = Column(
		String(255),
		comment="""ID of camera used for photos"""
		)
	Comment = Column(
		Text
		)
	Declination = Column(
		Float(8),
		default=7,
		comment="""Magnetic declination in degrees"""
		)
	EventDate = Column(
		DateTime,
		nullable=False
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	FuelsObserver = Column(
		String(25)
		)
	FuelsRecorder = Column(
		String(25)
		)
	MonitoringStatus = Column(
		String(25)
		)
	NumTransect = Column(
		Integer,
		default=1
		)
	PlotID = Column(
		String(50),
		nullable=False
		)
	PlotObserver = Column(
		String(25)
		)
	PlotRecorder = Column(
		String(25)
		)
	TreeObserver = Column(
		String(25)
		)
	TreeRecorder = Column(
		String(25)
		)
	VisitID = Column(
		String(255)
		)


class Fuels1000Hr(RiparianBase):
	__tablename__ = 'Fuels1000Hr'

	Comment = Column(
		String(255),
		comment="""Additional comments"""
		)
	DecayClass = Column(
		String(10),
		comment="""Decay class of fuel"""
		)
	Diameter = Column(
		Integer,
		comment="""Diameter of fuel"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	LogNum = Column(
		Integer,
		primary_key=True,
		comment="""Number of 1000 hr fuel""",
		nullable=False
		)
	Transect = Column(
		Integer,
		primary_key=True,
		comment="""Transect on which fuel was found""",
		nullable=False
		)


class FuelsDuffLitter(RiparianBase):
	__tablename__ = 'FuelsDuffLitter'

	Comment = Column(
		String(100)
		)
	DuffDepth = Column(
		Float(8)
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	FuelbedDepth = Column(
		Float(8)
		)
	LitterDepth = Column(
		Float(8)
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


class FuelsFine(RiparianBase):
	__tablename__ = 'FuelsFine'

	Comment = Column(
		String(100),
		comment="""Additional comments"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	HundredHour = Column(
		Integer,
		comment="""100Hr Fuels Count"""
		)
	OneHour = Column(
		Integer,
		comment="""1Hr Fuels count"""
		)
	Slope = Column(
		Integer,
		comment="""Slope of fuel line"""
		)
	TenHour = Column(
		Integer,
		comment="""10Hr Fuels count"""
		)
	Transect = Column(
		Integer,
		primary_key=True,
		comment="""Event transect ID""",
		nullable=False
		)


class GroundCover(RiparianBase):
	__tablename__ = 'GroundCover'

	BareSoil = Column(
		Float(8)
		)
	Bole = Column(
		Float(8)
		)
	Comment = Column(
		String(100)
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	Gravel = Column(
		Integer
		)
	Litter = Column(
		Float(8)
		)
	PlantBasal = Column(
		Float(8)
		)
	Rock = Column(
		Float(8)
		)


class nmramBiotic(RiparianBase):
	__tablename__ = 'nmramBiotic'

	Comments = Column(
		String(255),
		comment="""Additional comments"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	InvCover = Column(
		Integer,
		comment="""Invasive species percent cover"""
		)
	InvSpp = Column(
		String(255),
		comment="""Invasive species: list codes"""
		)
	PolyID = Column(
		Integer,
		primary_key=True,
		comment="""polygon in project area""",
		nullable=False
		)
	RegenCover = Column(
		Integer,
		comment="""Tree regeneration percent cover"""
		)
	StrucType = Column(
		String(255),
		comment="""Structure type"""
		)
	WetSpp = Column(
		String(255),
		comment="""Wetlands species: list codes"""
		)


class nmramComp(RiparianBase):
	__tablename__ = 'nmramComp'

	Comment = Column(
		String(100)
		)
	CT = Column(
		String(5),
		primary_key=True,
		nullable=False
		)
	CTRaw = Column(
		Float(8)
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	HerbSpp1 = Column(
		String(6)
		)
	HerbSpp2 = Column(
		String(6)
		)
	HerbSppEN1 = Column(
		String(1)
		)
	HerbSppEN2 = Column(
		String(1)
		)
	PercArea = Column(
		Integer
		)
	PolyID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	ShortWoodEN1 = Column(
		String(1)
		)
	ShortWoodEN2 = Column(
		String(1)
		)
	ShortWoodSpp1 = Column(
		String(6)
		)
	ShortWoodSpp2 = Column(
		String(6)
		)
	TallWoodEN1 = Column(
		String(1)
		)
	TallWoodEN2 = Column(
		String(1)
		)
	TallWoodSpp1 = Column(
		String(6)
		)
	TallWoodSpp2 = Column(
		String(6)
		)
	WtScore = Column(
		Float(8)
		)


class nmramCover(RiparianBase):
	__tablename__ = 'nmramCover'

	AbioticCond = Column(
		Text,
		comment="""Abiotic condition (SA Description)"""
		)
	BioticCond = Column(
		Text,
		comment="""Biotic condition: vegetation patterns, composition and structure, exotics and invasives, disturbance evidence, fire and herbivory (SA Description)"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	LandContext = Column(
		Text,
		comment="""Landscape context: summarize the wetland and surrounding landscape (SA Description)"""
		)


class nmramPolygon(RiparianBase):
	__tablename__ = 'nmramPolygon'

	Comment = Column(
		String(255),
		comment="""Additional comments"""
		)
	DateCreated = Column(
		DateTime,
		comment="""Date created"""
		)
	Description = Column(
		String(255),
		comment="""Brief description"""
		)
	PolygonID = Column(
		String(255),
		primary_key=True,
		comment="""Monitoring contractor ID/polygon standard ID""",
		nullable=False
		)
	PolyName = Column(
		String(255),
		comment="""Name of the polygon"""
		)
	Project = Column(
		String(255),
		comment="""Project ID that current polygon falls under"""
		)


class nmramScores(RiparianBase):
	__tablename__ = 'nmramScores'

	CTScore = Column(
		Float(8),
		comment="""Weighted CT score for entire area"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	Fuels = Column(
		String(255),
		comment="""Surface fuels rating (Table 8)"""
		)
	HorizStruct = Column(
		Integer,
		comment="""Ratings for overall vegetation horizontal path structure (B2)"""
		)
	InvCover = Column(
		Integer,
		default=0,
		comment="""Rating for invasive exotic plant species cover (Table B5)"""
		)
	NativeCommComp = Column(
		Integer,
		comment="""Relative native plant community composition rating (B1)"""
		)
	PercInvCover = Column(
		Float(8),
		comment="""Percent invasive species cover (Worksheet 9)"""
		)
	SoilCond = Column(
		Integer,
		comment="""Soil surface condition rating (Table 7)"""
		)
	TreeRegen = Column(
		Integer,
		comment="""Native riparian tree regeneration rating (B4)"""
		)
	VertStruct = Column(
		Integer,
		comment="""Rating for vegetation vertical structure (B3)"""
		)


class nmramScoreWts(RiparianBase):
	__tablename__ = 'nmramScoreWts'

	HorizStruct = Column(
		Float(8),
		comment="""Weight for overall vegetation horizontal path structure (B2)"""
		)
	ID = Column(
		Integer,
		primary_key=True
		)
	InvCover = Column(
		Float(8),
		comment="""Weight for invasive exotic plant species cover (Table B5)"""
		)
	NativeCommComp = Column(
		Float(8),
		comment="""Weight for native plant community composition rating (B1)"""
		)
	TreeRegen = Column(
		Float(8),
		comment="""Weight for native riparian tree regeneration rating (B4)"""
		)
	VertStruct = Column(
		Float(8),
		comment="""Weight for vegetation vertical structure (B3)"""
		)


class nmramStructArea(RiparianBase):
	__tablename__ = 'nmramStructArea'

	Area1 = Column(
		Integer,
		comment="""Total % of project area for structural type 1 (Worksheet 8)"""
		)
	Area2 = Column(
		Integer,
		comment="""Total % of project area for structural type 2 (Worksheet 8)"""
		)
	Area5 = Column(
		Integer,
		comment="""Total % of project area for structural type 5 (Worksheet 8)"""
		)
	Area6H = Column(
		Integer,
		comment="""Total % of project area for structural type 6H (Worksheet 8)"""
		)
	Area6S = Column(
		Integer,
		comment="""Total % of project area for structural type 6S (Worksheet 8)"""
		)
	Area6W = Column(
		Integer,
		comment="""Total % of project area for structural type 6W (Worksheet 8)"""
		)
	Area7 = Column(
		Integer,
		comment="""Total % of project area for structural type 7 (Worksheet 8)"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)


class PhotoLog(RiparianBase):
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
		Float(8),
		default=0,
		comment="""Distance from photo target (default in feet)"""
		)
	DistanceUnits = Column(
		String(255),
		default="""Feet""",
		comment="""Default units for distance"""
		)
	EventID = Column(
		String(50),
		comment="""Event ID""",
		nullable=False
		)
	ForeDesc = Column(
		Text,
		comment="""Foreground descriptors"""
		)
	Lat = Column(
		Float(8),
		comment="""Latitude of photo location (dd.ddd)"""
		)
	Long = Column(
		Float(8),
		comment="""Longitude of the photo location (ddd.ddd)"""
		)
	PhotoID = Column(
		String(50),
		primary_key=True,
		comment="""ID of the photo""",
		nullable=False
		)
	PhotoNum = Column(
		String(25),
		comment="""Photo ID produced by the camera"""
		)


class Plot(RiparianBase):
	__tablename__ = 'Plot'

	AdminUnit = Column(
		String(50)
		)
	Aspect = Column(
		String(1),
		comment="""Aspect of plot, derived from azimuth"""
		)
	Azimuth = Column(
		Integer,
		default=0,
		comment="""Azimuth of primary slope in plot"""
		)
	Comment = Column(
		Text,
		comment="""Additional comments"""
		)
	CoordX = Column(
		Float(8),
		default=0,
		comment="""Decimal degree X coordinates of plot center"""
		)
	CoordY = Column(
		Float(8),
		default=0,
		comment="""Decimal degree Y coordinates of plot center"""
		)
	DateCreated = Column(
		DateTime,
		comment="""Date plot created"""
		)
	Elevation = Column(
		Integer,
		comment="""Elevation of plot"""
		)
	ElevationUnits = Column(
		String(10),
		default="""Feet""",
		comment="""Units for elevation; defaults to feet"""
		)
	MacroPlot = Column(
		Float(8),
		comment="""Macro plot size (outer plot) in acres"""
		)
	MicroPlot = Column(
		Float(8),
		comment="""Micro plot size (inner plot) in acress"""
		)
	Orient16 = Column(
		String(255),
		comment="""Orientation of short side of plot (if BEMP)"""
		)
	Orient98 = Column(
		String(255),
		comment="""Orientation of long side of plot (if BEMP)"""
		)
	PlotID = Column(
		String(50),
		primary_key=True,
		comment="""Plot ID""",
		nullable=False
		)
	PlotName = Column(
		String(255),
		comment="""Name of the plot"""
		)
	PlotType = Column(
		String(255),
		comment="""what type of plot this is (BEMP, Fuels)"""
		)
	ProjectID = Column(
		String(50),
		comment="""GRGWA project ID"""
		)
	Slope = Column(
		Integer,
		default=0,
		comment="""Slope angle of primary plot direction"""
		)


class Project(RiparianBase):
	__tablename__ = 'Project'

	Comment = Column(
		Text,
		comment="""Any additional comments"""
		)
	Community = Column(
		String(255),
		comment="""nearest town/area"""
		)
	County = Column(
		String(255),
		comment="""county where project is located"""
		)
	DateCreated = Column(
		DateTime,
		comment="""Date the project entry was created"""
		)
	Description = Column(
		String(255),
		comment="""Brief description of the project"""
		)
	Owner = Column(
		String(255),
		comment="""specify owner"""
		)
	OwnershipType = Column(
		String(255),
		comment="""Tribal, Private, etc."""
		)
	ProjectID = Column(
		String(255),
		primary_key=True,
		comment="""Standard project ID""",
		nullable=False
		)
	ProjectName = Column(
		String(255),
		comment="""Name of the project"""
		)
	SWCD = Column(
		String(255),
		comment="""Sponsor (soil and water conservation district)"""
		)


class ProjectComment(RiparianBase):
	__tablename__ = 'ProjectComment'

	AccessConcerns = Column(
		Text,
		comment="""briefly describe any site access concerns"""
		)
	Assessment = Column(
		Text,
		comment="""Could treatment of the project have been done better? How?"""
		)
	CommentsNotes = Column(
		Text,
		comment="""other comments or notes"""
		)
	ProjectID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)


class SiteType(RiparianBase):
	__tablename__ = 'SiteType'

	Acres = Column(
		Integer,
		default=0
		)
	ESName = Column(
		String(255)
		)
	ProjectID = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	ProjPercent = Column(
		Integer,
		default=0
		)
	SiteType = Column(
		String(255)
		)


class Soils(RiparianBase):
	__tablename__ = 'Soils'

	Aspect = Column(
		String(255),
		primary_key=True,
		comment="""Aspect at which soil was collected""",
		nullable=False
		)
	EventID = Column(
		String(255),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	SoilType = Column(
		String(255),
		comment="""Soil Texture type"""
		)


class Species(RiparianBase):
	__tablename__ = 'Species'

	BaseSymbol = Column(
		String(7),
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
		String(7),
		primary_key=True,
		comment="""Used USDA symbol""",
		nullable=False
		)
	SynSymbol = Column(
		String(7),
		comment="""USDA synonym (used for subspecies and variations)"""
		)


class StructClass(RiparianBase):
	__tablename__ = 'StructClass'

	EventID = Column(
		String(255),
		primary_key=True,
		comment="""EventID""",
		nullable=False
		)
	Modified = Column(
		String(255),
		comment="""H & O modified dominant structure class"""
		)
	Original = Column(
		String(255),
		comment="""H & O original dominant structure class"""
		)


class Transect(RiparianBase):
	__tablename__ = 'Transect'

	Azimuth = Column(
		Integer,
		default=0,
		comment="""Transect Azimuth"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	Length = Column(
		Float(8),
		default=75,
		comment="""Transect length (defaults to 75)"""
		)
	Slope = Column(
		Integer,
		default=0,
		comment="""Slope along transect"""
		)
	Transect = Column(
		Integer,
		primary_key=True,
		default=0,
		comment="""Transect Number""",
		nullable=False
		)


class Treatments(RiparianBase):
	__tablename__ = 'Treatments'

	AcresPlanned = Column(
		String(255),
		comment="""how many acres were planned for treatment"""
		)
	AcresTreated = Column(
		String(255),
		comment="""how many acres were successfully treated"""
		)
	AvgMasticationDepth = Column(
		String(255),
		comment="""inches of average mastication depth from inspection report"""
		)
	AvgPercentMastication = Column(
		String(255),
		comment="""average percent mastication ground cover from inspection report"""
		)
	ChemAdherencetoGuidelines = Column(
		Boolean,
		default=False,
		comment="""were chemical guidelines adhered to during treatment?"""
		)
	ChemComments = Column(
		Text,
		comment="""comments on chemical use during treatment?"""
		)
	ChemConUsed = Column(
		String(255),
		comment="""concentration of chemical used during treatment"""
		)
	ChemUsed = Column(
		String(255),
		comment="""chemical used during treatment"""
		)
	ContractAward = Column(
		DateTime,
		comment="""date treatment contract awarded"""
		)
	Contractor = Column(
		String(255),
		comment="""Name of contractor awarded treatment contract"""
		)
	CostContractAward = Column(
		Integer,
		default=0,
		comment="""cost of contract awarded"""
		)
	DateTxCompleted = Column(
		DateTime,
		comment="""date this treatment was completed"""
		)
	DateTxStarted = Column(
		DateTime,
		comment="""date this treatment began"""
		)
	Desiredcondition = Column(
		String(255),
		comment="""what was the site's desired condition following treatment?"""
		)
	DifferenceImpl = Column(
		Boolean,
		default=False,
		comment="""were there any differences between the planned and the implemented treatment?"""
		)
	Differencesinfo = Column(
		Text,
		comment="""explain the differences between planned and implemented treatment"""
		)
	ID = Column(
		Integer,
		primary_key=True
		)
	InvasivesonSitenotTargeted = Column(
		Boolean,
		default=False,
		comment="""were there invasives on site not targeted during treatment?"""
		)
	MechanicalTreatment = Column(
		String(255),
		comment="""method of mechanical treatment used"""
		)
	notTargetedinfo = Column(
		Text,
		comment="""information about invasives not targeted during treatment"""
		)
	OriginalProposalDate = Column(
		DateTime,
		comment="""when was this treatment originally proposed to grgwa?"""
		)
	PercentTargetSppRemoved = Column(
		String(255),
		comment="""what percentage of target invasives were removed during treatment?"""
		)
	Planting = Column(
		Boolean,
		default=False,
		comment="""was planting was of the treatment plan?"""
		)
	PlantingInfo = Column(
		Text,
		comment="""information on planting that occurred"""
		)
	ProjectGoals = Column(
		Text,
		comment="""main goals from project proposals"""
		)
	ProjectID = Column(
		String(255),
		nullable=False
		)
	ProjectSuccess = Column(
		Boolean,
		default=False,
		comment="""was project considered successful by all partners?"""
		)
	SlashTreatment = Column(
		String(255),
		comment="""how was slash handled during treatment?"""
		)
	SpecialConsidNativeTrees = Column(
		String(255),
		comment="""details on any special considerations taken for native trees?"""
		)
	TargetSpp = Column(
		String(255),
		comment="""what were the target species of treatment?"""
		)
	TxCategory = Column(
		String(255),
		comment="""what category of treatment is this"""
		)
	TxComments = Column(
		Text,
		comment="""additional information on treatment"""
		)


class TreesIndv(RiparianBase):
	__tablename__ = 'TreesIndv'

	CharHeight = Column(
		Float(8),
		comment="""Height of any char on the tree"""
		)
	Comment = Column(
		String(255),
		comment="""Additional comments"""
		)
	DamageCode1 = Column(
		String(10),
		comment="""Type of damage to tree - 1"""
		)
	DamageCode2 = Column(
		String(10),
		comment="""Type of damage to tree - 2"""
		)
	DamageCode3 = Column(
		String(10),
		comment="""Type of damage to tree - 3"""
		)
	DamageCode4 = Column(
		String(10),
		comment="""Type of damage to tree - 4"""
		)
	DamageCode5 = Column(
		String(10),
		comment="""Type of damage to tree - 5"""
		)
	DamageSev1 = Column(
		String(10),
		comment="""Severity of damage - 1"""
		)
	DamageSev2 = Column(
		String(10),
		comment="""Severity of damage - 2"""
		)
	DamageSev3 = Column(
		String(10),
		comment="""Severity of damage - 3"""
		)
	DamageSev4 = Column(
		String(10),
		comment="""Severity of damage - 4"""
		)
	DamageSev5 = Column(
		String(10),
		comment="""Severity of damage - 5"""
		)
	DBH = Column(
		Float(8),
		comment="""Diameter at breast height (in inches)"""
		)
	DRC = Column(
		Float(8),
		comment="""Diameter at root crown"""
		)
	EventID = Column(
		String(50),
		primary_key=True,
		comment="""Event ID""",
		nullable=False
		)
	Height = Column(
		Float(8),
		comment="""Tree height (in feet)"""
		)
	LCBH = Column(
		Float(8),
		comment="""Live crown base height (in feet)"""
		)
	Mistletoe = Column(
		Float(8),
		comment="""Percentage of tree infected with mistletoe"""
		)
	NuDeStems = Column(
		Integer,
		comment="""Number of dead stems"""
		)
	NuLiStems = Column(
		Integer,
		comment="""Number of live stems"""
		)
	ScorchHeight = Column(
		Float(8),
		comment="""Height of scorch on the tree"""
		)
	Species = Column(
		String(255),
		primary_key=True,
		comment="""Species code""",
		nullable=False
		)
	Status = Column(
		String(255),
		comment="""Tree status: live or dead"""
		)
	StemNum = Column(
		Integer,
		primary_key=True,
		default=0,
		comment="""Number of stems on tree""",
		nullable=False
		)
	TagNum = Column(
		Integer,
		primary_key=True,
		default=0,
		comment="""Tree number for plot/event""",
		nullable=False
		)


class TreesSaplings(RiparianBase):
	__tablename__ = 'TreesSaplings'

	Count = Column(
		Integer
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	SizeClassDiam = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Species = Column(
		String(6),
		primary_key=True,
		nullable=False
		)
	Status = Column(
		String(2),
		primary_key=True,
		nullable=False
		)


class TreesSeedlings(RiparianBase):
	__tablename__ = 'TreesSeedlings'

	Count = Column(
		Integer
		)
	EventID = Column(
		String(50),
		primary_key=True,
		nullable=False
		)
	SizeClassHt = Column(
		String(255),
		primary_key=True,
		nullable=False
		)
	Species = Column(
		String(6),
		primary_key=True,
		nullable=False
		)
	Status = Column(
		String(255),
		primary_key=True,
		nullable=False
		)


class VegResponse(RiparianBase):
	__tablename__ = 'VegResponse'

	DamagetoNativesInfo = Column(
		Text,
		comment="""What damage is noted on native species? What species?"""
		)
	DamagetoNativeSpp = Column(
		Boolean,
		default=False,
		comment="""Is there collateral damage to native species on site?"""
		)
	LeftSppList = Column(
		String(255),
		comment="""targets intentionally left on site"""
		)
	LeftTreesnoted = Column(
		Boolean,
		default=False,
		comment="""Were the target species noted left intentionally?"""
		)
	LivestockUse = Column(
		Boolean,
		default=False,
		comment="""Evidence of livestock use following treatment?"""
		)
	LivestockUseComments = Column(
		Text,
		comment="""any other information/notes on livestock use?"""
		)
	LivestockUseIntensity = Column(
		String(255),
		comment="""Intensity of livestock utilization recorded on site"""
		)
	MissedSppList = Column(
		String(255),
		comment="""missed species on site"""
		)
	MissedTreesnoted = Column(
		Boolean,
		default=False,
		comment="""Were the target species missed by initial treatment?"""
		)
	NativeVegResponse = Column(
		String(255),
		comment="""NEED TO FIGURE OUT HOW TO DO THIS MORE"""
		)
	PrimaryLandUse = Column(
		String(255),
		comment="""primary land use noted during site visit"""
		)
	PrimaryLandUseComments = Column(
		Text,
		comment="""any other information on primary land use, or history of land use on site?"""
		)
	ProjectID = Column(
		String(255),
		nullable=False
		)
	ProjectMaintbyLO = Column(
		Boolean,
		default=False,
		comment="""Was the project maintained by the landowner?"""
		)
	ProjectMaintbyLOInfo = Column(
		String(255),
		comment="""Information on project maintenance actions undertaken by landowner?"""
		)
	ProjectMaintbySWCD = Column(
		Boolean,
		default=False,
		comment="""Was the project maintained by the SWCD?"""
		)
	ProjectMaintbySWCDInfo = Column(
		Text,
		comment="""Information on project maintenance actions undertaken by SWCDs"""
		)
	Resproutsnoted = Column(
		Boolean,
		default=False,
		comment="""Were there resprouts ?"""
		)
	ResproutsSppList = Column(
		String(255),
		comment="""target species resprouting on site"""
		)
	SiteRemediationInfo = Column(
		Text,
		comment="""Information on site remediation actions"""
		)
	SiteRemediationPostTx = Column(
		Boolean,
		default=False,
		comment="""Were there site remediation actions taken post-treatment?"""
		)
	TargetSppList = Column(
		String(255),
		comment="""target species on site"""
		)
	Targetspponsite = Column(
		Boolean,
		default=False,
		comment="""Were there target species on site during post-treatment site visit?"""
		)
	TargetspponsiteInfo = Column(
		Text,
		comment="""Other information on target species found on site"""
		)
	VisitID = Column(
		String(255),
		primary_key=True,
		comment="""what site visit was this?""",
		nullable=False
		)


class Visits(RiparianBase):
	__tablename__ = 'Visits'

	BEMP = Column(
		Boolean,
		default=False,
		comment="""If BEMP data was collected"""
		)
	Comment = Column(
		String(255)
		)
	Documents = Column(
		String(255),
		comment="""primary document produced as a result of this visit"""
		)
	Fuels = Column(
		Boolean,
		default=False,
		comment="""If fuels data was collected"""
		)
	NMRAM = Column(
		Boolean,
		default=False,
		comment="""If NMRAM data was collected"""
		)
	Photos = Column(
		Boolean,
		default=False,
		comment="""were photographs taken and saved for later use?"""
		)
	ProjectID = Column(
		String(255)
		)
	Trees = Column(
		Boolean,
		default=False,
		comment="""If overstory data was collected"""
		)
	VisitDate = Column(
		DateTime,
		comment="""date of the site visit"""
		)
	VisitID = Column(
		String(255),
		primary_key=True,
		comment="""create a unique site visit ID for this visit. Use project ID + first letter(s) of type + mmdd""",
		nullable=False
		)
	VisitLead = Column(
		String(255),
		comment="""who was responsible for the site visit (would have information)"""
		)
	VisitType = Column(
		String(255),
		comment="""what was the purpose of the site visit?"""
		)


class WitnessTree(RiparianBase):
	__tablename__ = 'WitnessTree'

	AzFromPc = Column(
		Integer
		)
	Comment = Column(
		String(100)
		)
	ConditionNotes = Column(
		String(100)
		)
	Dbh = Column(
		Float(8)
		)
	DistFromPc = Column(
		Integer
		)
	EventID = Column(
		String(25),
		primary_key=True,
		nullable=False
		)
	FlagColor = Column(
		String(10)
		)
	Height = Column(
		Float(8)
		)
	LCBH = Column(
		Float(8)
		)
	TreeTag = Column(
		Integer,
		primary_key=True,
		nullable=False
		)
	WitCondition = Column(
		String(10)
		)
	WitSpecies = Column(
		String(7)
		)

