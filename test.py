import gensim
from summarizer import summarize_nepali

sample_text = ''' १७ साउन, बुटवल । डिवाईसी सियारी-१ रुपन्देहीको कोटिहवामा जारी १८ औं लिस्नु कप फुटबल प्रतियोगिताको सेमिफाइनलमा प्रवेश गरेको छ ।

पशुपति माविको मैदानमा बिहीबार सम्पन्न अन्तिम क्वार्टरफाइनल खेलमा न्यू सिर्जना युवा क्लब करौजियालाई शून्यका विरुद्ध ५ गोलले पराजित गर्दै डिवाईसी सियारी-१ सेमिफाइनलमा प्रवेश गरेेको होे ।

डिवाईसीको जितको लागि विदेशी खेलाडी म्याक्सले खेलको पहिलो हाफको १० औं मिनेट, दोस्रो हाफको ३३ औं मिनेटमा १/१ गोल, जनक कार्कीले खेलको पहिलो हाफकोे १६ औं मिनेटमा १ गोल र राज पौडेलले दोस्रो हाफको १०औं र २५औं मिनेटमा १/१ गोल गरेका थिए । बिहीबार सम्पन्न खेलको म्यान अफ द म्याच डिवाइसीका दिपेश श्रेष्ठ घोषित भएका थिए ।

प्रतियोगिता अन्तर्गत शुक्रबार सेमिफाइनलका खेल सुरुवात हुँदैछ । पहिलो सेमिफाइनल खेल आयोजक लिस्नु युवा क्लब कोटिहवा र नवयुवा खेलकुद तथा सांस्कृतिक परिवार ठुटिपिपलबीच हुने आयोजक लिस्नु युवा क्लबका सचिव मनोज क्षत्रीले जानकारी दिए ।

साउन २१ गते सम्म सञ्चालन हुने प्रतियोगिताको विजेताले तीन लाख, उपविजेताले एक लाख ५० हजार र सेमिफाइनलमा पुग्ने दुई टिमले २५ हजारका दरले नगद पुरस्कार प्राप्त गर्नेछन् । प्रतियोगितामा भारतको मुम्बईस्थित फुटबल क्लब दादर ११ सहित रुपन्देही, नवलपरासी, दाङ, स्याङ्जा र चितवनका गरी १६ टिमले भाग लिएका छन् । '''

print(summarize_nepali(sample_text))



				