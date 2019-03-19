from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # ฟ้าต้องทำการตอบคำถามที่เป็นการบ้านของเธอ
        # เธอจึงเปิดหน้าเว็บขึ้นมา แล้วไปยัง URL ที่เธอได้ลิ้งจากอาจารย์
        self.browser.get('http://localhost:8000/')

        # เมื่อเข้าไปในหน้าเว็บ เธอพบว่ามี 2 คำถามที่เธอต้องเลือกตอบ
        table = self.browser.find_element_by_tag_name('table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertEqual(2,len(rows)-1)
   
        # เธอจึงไปมองไปที่คำถามแรก และมีการแสดงตัวเลือกให้เห็นด้วย
        self.assertIn("Where're you from?", rows[1].text)
        self.assertIn("Thailand", rows[1].text)
        self.assertIn("China", rows[1].text)

        # เธอกดไปที่คำถามแรก
        first_question = table.find_elements_by_tag_name('a')[0]
        first_question.send_keys(Keys.ENTER)
        time.sleep(1)

        # เมื่อหน้าเว็บโหลดเสร็จ เธอเห็นว่าหน้าเว็บแสดงคำถาม และมีตัวเลือกสองตัวให้เธอเลือก
        header_text = self.browser.find_element_by_tag_name('h1').text 
        self.assertIn("Where're you from?", header_text)
        choices = self.browser.find_elements_by_tag_name('label')
        self.assertEqual(2,len(choices))
        
        # เธอจึงเลือกที่คำว่า 'Thailand' 
        self.assertEqual("Thailand",choices[0].text)
        first_choice = self.browser.find_elements_by_name('choice')[0]
        first_choice.click()
        
        # แล้วกดปุ่ม vote ทันที
        # ทำให้หน้าเว็บแสดงหน้าใหม่ขึ้นมา เธอเห็นเป็นข้อความคำถามเมื่อเดิม
        # และเธอพบว่ามีคะแนนโหวตของตัวเลือกที่เธอเลือกมีค่าเป็นสาม 
        # ส่วนอีกตัวเลือกมีผลโหวตเป็นศูนย์
        # เนื่องจากเพื่อนของเธอ ฝากให้เธอช่วยตอบคำถามแทนให้ด้วย เธอจึงกดไปที่ vote again?
        # เพื่อนของเธอเป็นคนจีน เธอจึงเลือกตัวเลือกที่เป็น 'China'
        # แล้วกดปุ่มโหวตอีกคร้้ง
        # ทำให้หน้าผลโหวตที่ตอนแรกตัวเลือก 'China' เป็น 0 มีค่าเป็นหนึ่งแทน
        # หลังจากที่เธอตอบคำถามเสร็จเธอจึงปิดคอมเข้านอน เพื่อไปโรงเรียนแต่เช้า

        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
