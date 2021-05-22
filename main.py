import os
import time
import datetime

import pyrogram

user_session_string = "BQBvCMCvsvnHZ5bj9qdsBaxn2hDcEboH7J-fui-eJoHc9nh_7BW65_reTflsHchKCCcpRii_K1zwbzOpNoKpikIinsSVhWjOFpegXNTHjmW5vhTCvuTPJWVkNO4h-tCrVmcTnUSPu1pU6FXiBxBQ665poGvfiJJD2b4YvF2suG7N9tNimLTcHvTsGjVfsbZprdNxqTvSPjiO_doNdh3TPTJFCgEXJfCJVnPwbhoFOdx93saqzj5SJ55LD4m-2VWYSlu9UTRrRbT2WL6OJgPDRHssjf_kqcSrOrRjPVrmzV-nkL0K_v8BYjOSSgftD3k18RQ7aKXGF0JL93EI42BYOlbgQnwTKAA"
bots = ["WhiteEyeRenameBot", "WhiteEyeURLUploaderBot", "WhiteEyeTelegraphBot", "WhiteEyeSubtitleBot", "WhiteEyeYouTubeBot", "WhiteEyeForceSubscriberBot", "WhiteEyeTagRemoverBot", "WhiteEyeDeleteAllBot", "WhiteEyeCompressorBot", "WhiteEyeURLShortnerBot"]
bot_owner = "@Newton_TG"
update_channel = "@whiteeyebots"
status_message_id = "655292"
api_id = "2618494"
api_hash = "18037dd93c54961ec67c8a9ecbc1d682"

user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)


user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)


def main():
    with user_client:
        while True:
            print("[INFO] starting to check uptime..")
            edit_text = f" All Bot List And Online Status. \n\n💡𝘉𝘰𝘵 𝘜𝘱𝘥𝘢𝘵𝘦𝘥 𝘌𝘷𝘦𝘳𝘺 1 HOurs n\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(15)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"**➩ @{bot}**    `❌`\n"
                    user_client.send_message(bot_owner,
                                             f"@{bot} status: `Down`")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"**➩ @{bot}**    `✅`\n"
                user_client.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"\n Last Updated And Checked On: \n\n__{str(ist_now)}__ 🇮🇳 IST\n__{utc_now}__ 🌎 UTC"

            user_client.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            print(f"[INFO] everything done! sleeping for 15 mins...")

            time.sleep(59 * 60)


main()
