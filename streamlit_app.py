import streamlit  as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="NAIL DISEASE DETECTOR", page_icon=":medical_symbol:", layout="wide")

tb1, tb2 =st.tabs(["HOME", "DISEASE DETECTOR"])

with tb1:
	st.title(":medical_symbol: NAIL DISEASE DETECTOR")
	st.write("---")
	st.header("NAILS AND THEIR IMPORTANCE")
	st.write(
		"""
		Nails are protective structures composed of a protein called keratin that grow at the tips of the fingers and toes in humans and other mammals. They serve several important functions:

	- Protection: Nails provide protection to the sensitive tips of the fingers and toes. They act as a shield to prevent injuries or damage to the underlying tissues.
	- Sensory Function: Nails also have a sensory function, particularly in the fingertips where they play a role in tactile sensation. The fingertips are highly sensitive, and nails help enhance touch perception.
	- Grip and Manipulation: Nails enhance our ability to grip and manipulate objects. They provide a firm, non-slip surface that helps us hold onto items, such as when picking up small objects or opening containers.
	- Scratching: Nails can be used for scratching, which can be a useful function for relieving itching or removing debris from the skin.
	- Health Indicator: The appearance of nails can sometimes serve as an indicator of overall health. Changes in nail color, texture, or growth patterns can be associated with various health conditions or nutritional deficiencies.
	- Cosmetic and Aesthetic Value: For many people, well-maintained nails are an important aspect of personal grooming and aesthetics. Manicures and pedicures are popular beauty treatments to enhance the appearance of nails.
		"""
	)
	st.header("NAIL DISEASES")
	st.write(
		"""
		Nails can sometimes provide clues about a person's health, and certain changes in nail appearance may be indicative of underlying medical conditions. Here are some nail-related conditions and the information they can provide:

	- Fungal Nail Infections (Onychomycosis): Fungal nail infections are common and can affect one or more nails. They often appear as discolored, thickened, and brittle nails. Fungal infections are typically caused by dermatophytes, yeast, or molds. Treatment may include topical or oral antifungal medications.
	- Psoriasis: Psoriasis is a chronic skin condition that can also affect the nails. Nail psoriasis can cause pitting, discoloration, and separation of the nail from the nail bed. It is often associated with skin psoriasis and can be treated with topical steroids or other psoriasis medications.
	- Eczema (Dermatitis): Eczema can affect the skin around the nails, leading to redness, swelling, and peeling of the skin. This condition may be associated with itching and discomfort. Managing eczema with moisturizers and topical corticosteroids can help alleviate symptoms.
	- Ingrown Nails (Onychocryptosis): Ingrown nails occur when the edges of the nails grow into the surrounding skin, causing pain, redness, and inflammation. Proper nail trimming and avoiding tight-fitting footwear can help prevent ingrown nails. In severe cases, minor surgical procedures may be required.
	- Beau's Lines: Beau's lines are transverse depressions or ridges that run horizontally across the nails. They can be caused by a variety of factors, including illness, trauma, or nutritional deficiencies. The appearance of Beau's lines can offer insight into the timing of an underlying health issue.
	- Yellow Nail Syndrome: Yellow nail syndrome is a rare condition that can cause nails to thicken, yellow, and grow more slowly. It may be associated with lymphedema and respiratory issues. Identifying and managing the underlying causes of the syndrome is crucial.
	- Clubbing: Nail clubbing is characterized by an enlargement of the fingertips and a downward curving of the nails. It can be associated with various lung and heart conditions. If clubbing is observed, it is important to consult a healthcare professional to identify and address the underlying issue.
	- Koilonychia: Koilonychia is a condition where the nails become concave or spoon-shaped. It can be a sign of iron-deficiency anemia or hemochromatosis, among other conditions. Treating the underlying cause is essential.
	- Nail Trauma: Physical trauma or repeated stress on the nails can lead to nail disorders or abnormalities. Proper nail care, protection, and avoiding excessive trauma can help maintain nail health.
	
	It's important to note that changes in the nails can result from various causes, and while they can offer valuable diagnostic clues, a healthcare professional or dermatologist should evaluate any persistent or concerning nail changes. These professionals can determine the underlying causes and recommend appropriate treatments or interventions.
		"""
	)
	st.header("WHY IS IT IMPORTANT TO DETECT THEM")
	st.write(
		"""
		- Early Intervention: Detecting nail diseases early can lead to more effective treatment and better outcomes. In many cases, early intervention can prevent the condition from worsening or spreading to other nails.
	- Underlying Health Issues: Changes in nail appearance can sometimes be a sign of underlying health conditions, such as fungal infections, psoriasis, or nutritional deficiencies. Identifying these signs can prompt further medical evaluation, which may lead to the diagnosis and treatment of other health problems.
	- Prevention: Identifying and treating nail diseases can help prevent complications. For example, fungal nail infections can lead to secondary bacterial infections or the spread of the infection to other parts of the body if left untreated.
	- Quality of Life: Nail diseases can be uncomfortable, painful, or unsightly. Addressing these conditions can improve a person's overall quality of life, reduce discomfort, and enhance self-esteem.
	- Infection Control: Some nail diseases, such as fungal infections, can be contagious. Prompt detection and treatment can help prevent the spread of these infections to others.
	- Avoiding Complications: Certain nail conditions, if left untreated, can lead to complications, such as cellulitis (a skin infection), abscesses, or chronic pain. Addressing these issues promptly can prevent these complications.
	- Monitoring Chronic Conditions: For individuals with chronic skin conditions like psoriasis or eczema, monitoring the nails is essential as they can be affected. Catching nail-related symptoms early allows for better management of the underlying skin condition.
	- Personal Grooming and Well-Being: Many people take pride in their personal grooming, and healthy nails are a part of that. Maintaining the health and appearance of nails can contribute to a person's overall well-being and self-confidence.
	"""
	)
	st.header("ABOUT THE CREATOR")
	st.write(
		"""
		Greetings! I'm Krishiv Mahajan, a passionate grade 11 student at Sat Paul Mittal School with a profound love for computer science and an unwavering desire to make a positive impact in people's lives. As I embark on this journey, my mission is crystal clear - to combine the power of technology with a heartfelt commitment to your well-being.
	In a world where health takes precedence, I've set out to create a dedicated space where your nail health is at the forefront. Nails are often the silent messengers of underlying health issues, and my aim is to empower you with the tools to detect diseases early and take control of your well-being.
	My dedication to the world of computer science fuels my pursuit of innovation and excellence. I believe that technology can be a force for good, and together, we can harness its potential to revolutionize how we care for our nails and, in turn, our overall health.
	With the Nail Disease Detection website, I aspire to provide a valuable resource for everyone. Whether you're seeking answers to your nail-related concerns or simply want to stay informed about your health, you'll find a supportive community here.
		"""
	)
	
with tb2:
	st.header("TEST YOURSELF")
	"""@st.cache_resource
	def LoadModel():
		mod=YOLO("File_nail.pt")
		return mod """
	img=st.file_uploader("UPLOAD THE IMAGE OF YOUR NAIL")
	if img is not None:
		col=st.columns(3)
		col[1].image(img)
		#img1=img.getvalue()
		img2=Image.open(img)
		"""model=LoadModel()
		res=model.predict(img2,verbose=False)
		label = res[0].probs.top5 
		conf = res[0].probs.top5conf
		conf = conf.tolist()
		col1,col2 = st.columns(2)
		with col1:
			st.subheader(res[0].names[label[0]].title())
			st.subheader(res[0].names[label[1]].title())
			st.subheader(res[0].names[label[2]].title())
			st.subheader(res[0].names[label[3]].title())
			st.subheader(res[0].names[label[4]].title())		
		with col2:
			st.subheader(str(round(conf[0]*100,2))+' Confidence')
			st.subheader(str(round(conf[1]*100,2))+' Confidence')
			st.subheader(str(round(conf[2]*100,2))+' Confidence')
			st.subheader(str(round(conf[3]*100,2))+' Confidence')
			st.subheader(str(round(conf[4]*100,2))+' Confidence')"""
		import inference
		model = inference.get_model("nail-diseases-wnxuv/1")
		pred=model.infer(
			image=img2,
			confidence=0.9
				)
		st.write(type(pred[0]))

