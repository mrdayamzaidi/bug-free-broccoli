import os
import time
import datetime

import pyrogram

user_session_string = "BQBvCMCvsvnHZ5bj9qdsBaxn2hDcEboH7J-fui-eJoHc9nh_7BW65_reTflsHchKCCcpRii_K1zwbzOpNoKpikIinsSVhWjOFpegXNTHjmW5vhTCvuTPJWVkNO4h-tCrVmcTnUSPu1pU6FXiBxBQ665poGvfiJJD2b4YvF2suG7N9tNimLTcHvTsGjVfsbZprdNxqTvSPjiO_doNdh3TPTJFCgEXJfCJVnPwbhoFOdx93saqzj5SJ55LD4m-2VWYSlu9UTRrRbT2WL6OJgPDRHssjf_kqcSrOrRjPVrmzV-nkL0K_v8BYjOSSgftD3k18RQ7aKXGF0JL93EI42BYOlbgQnwTKAA"
bots = ["WhiteEyeRenameBot", "WhiteEyeURLUploaderBot", "WhiteEyeTelegraphBot", "WhiteEyeSubtitleBot", "WhiteEyeYouTubeBot", "WhiteEyeForceSubscriberBot", "WhiteEyeTagRemoverBot", "WhiteEyeDeleteAllBot", "WhiteEyeCompressorBot", "WhiteEyeURLShortnerBot"]
bot_owner = "@WhiteEyeDevs"
update_channel = "@whiteeyebots"
status_message_id = "94"
api_id = "2618494"
api_hash = "18037dd93c54961ec67c8a9ecbc1d682"

user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)


def main():
    with user_client:
        while True:
            print("[INFO] Starting To Bots ♻️..")
            edit_text = f"@{update_channel} Bot's Uptime Status.(Updated every 1 hour)\n\n"
            for bot in bots:
                print(f"[INFO] Checking @{bot}")
                snt = user_client.send_message(bot, '/start')

                time.sleep(59)

                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} Is Down")
                    edit_text += f"@{bot} Status: `❌`\n\n"
                    user_client.send_message(bot_owner,
                                             f"@{bot} Status: `❌`")
                else:
                    print(f"[INFO] All Good With @{bot}")
                    edit_text += f"@{bot} Status: `✅`\n\n"
                user_client.read_history(bot)

            utc_now = datetime.datetime.utcnow()
            ist_now = utc_now + datetime.timedelta(minutes=30, hours=5)

            edit_text += f"__Last Checked On \n{str(utc_now)} UTC\n{ist_now} IST__"

            user_client.edit_message_text(update_channel, status_message_id,
                                         edit_text)
            print(f"[INFO] Status Updated!! Now Sleeping For 1 Hour.")

            time.sleep(15 * 60)


main()
