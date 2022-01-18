
import mysql.connector

class dbmysq:

    def __init__(self):
        self._cnx = mysql.connector.connect(
            user='phpmyadmin',
            password='shthyyKsbaZ65wkD',
            host='127.0.0.1',
            database='isphere'
        )
        self._cnx.autocommit=True
        self._cursor = self._cnx.cursor()
    def __enter__ (self):
        return self
    def __exit__(self,exc_type,exc_value, exc_tb):
        self.close()
    @property
    def cursor(self):
        return self._cursor
    @property
    def connection(self):
        return self._cnx


    def execute(self,sql,params=None):
        self.cursor.execute(sql,params or())
    
    # cursor = cnx.cursor()
    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)
    query1_30 = ("SELECT COUNT(*) count FROM isphere.session "
                "WHERE request_id IS NULL AND sessionstatusid=2"
                "AND (statuscode<>'used' OR unix_timestamp(now())-unix_timestamp(lasttime)>600) "
                "AND sourceid=55 AND captcha>'' AND statuscode<>'success'"
                )

    query2_36 = ("SELECT COUNT(*) count FROM isphere.session "
                "WHERE sessionstatusid=2 AND sourceid=55 "
                "AND unix_timestamp(now())-unix_timestamp(lasttime)>600")

    # query3_43 = ("UPDATE isphere.session s SET request_id=".$reqId.
    #             "WHERE request_id IS NULL AND ((sessionstatusid=2 AND (statuscode<>'used' "
    #             "OR unix_timestamp(now())-unix_timestamp(lasttime)>600)".($usecaptcha?
    #             " AND captcha>'' AND statuscode<>'success'": "").")".($uselocked?
    #             " OR (sessionstatusid=6 AND statuscode='tagslimitexceed')": "").
    #             ") AND sourceid=55 AND token>'' ORDER BY lasttime limit 1"
    #             )

    # query4_44 = ("SELECT id,cookies,starttime,lasttime,captcha,token,enckey,device,proxyid,"
    #             "(SELECT concat(server,':',port) FROM proxy WHERE id=s.proxyid) proxy,(SELECT concat(login,':',password) FROM proxy "
    #             "WHERE id=s.proxyid) proxy_auth FROM isphere.session s WHERE sourceid=55 AND request_id=".$reqId
    #             )

    # query5_66 = ("UPDATE isphere.session "
    #             "SET lasttime=now(),used=ifnull(used,0)+1,used_ext=ifnull(used_ext,0)+1,sessionstatusid=2,statuscode='used',request_id=NULL "
    #             "WHERE id=".$sessionData -> id

    #             )

    # query6_67 = ("UPDATE isphere.session SET lasttime=now(),used=ifnull(used,0)+1,used_ext=ifnull(used_ext,0)+1,sessionstatusid=2,statuscode='used',request_id=NULL "
    #             "WHERE statuscode<>'used' AND id=".$sessionData -> id
    #             )

    # query7_70 = ("SELECT id proxyid, concat(server,':',port) proxy, concat(login,':',password) proxy_auth, "
    #             "(SELECT count(*) FROM session s "
    #             "WHERE sourceid=55 AND proxyid=proxy.id) scnt FROM isphere.proxy "
    #             "WHERE enabled=1 AND status=1 AND country='ru' ORDER BY scnt limit 1"
    #             )

    # query8_78 = ("UPDATE isphere.proxy SET lasttime=now() "
    #             "WHERE id=".$row -> proxyid
    #             )

    # query9_79 = ("UPDATE isphere.session SET proxyid=".$row -> proxyid.
    #             " WHERE id=".$sessionData -> id
    #             )

    # query10_652 = ("UPDATE isphere.session SET statuscode='success' WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query11_664 = ("UPDATE isphere.session SET sessionstatusid=4,statuscode='invalidcaptcha',captchaimage='".$res['result']['image'].
    #             "' WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query12_669 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 5 day),sessionstatusid=6,statuscode='failed' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query13_673 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 year),sessionstatusid=6,statuscode='notauthorized' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query14_697 = ("INSERT INTO isphere.session (endtime,sourceid,sessionstatusid,statuscode,captcha,captcha_service,captcha_id) "
    #             "VALUES (now(),55,".($report == 'bad'?4: 3).",'".($report == 'bad'?'invalidcaptcha': 'success')."','".$captcha_value."','".$this -> captcha_service[$swapData['captcha_service']]['host']."','".$swapData['captcha_id']."')"
    #             )
    # query15_721 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 day),sessionstatusid=6,statuscode='failed' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query16_725 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 year),sessionstatusid=6,statuscode='notauthorized' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query17_749 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 day),sessionstatusid=6,statuscode='tagslimitexceed' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query18_761 = ("UPDATE isphere.session SET used=0,success=0,success_ext=ifnull(success_ext,0)+1,statuscode='success' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query19_772 = ("UPDATE isphere.session SET used=0,success=0,success_ext=ifnull(success_ext,0)+1,statuscode='success' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query20_775 = ("UPDATE isphere.session SET unlocktime=date_add(str_to_date('".date('Y-m-01 03:00:00', time()-3*60*60)."', '%Y-%m-%d %H:%i:%s'),interval 1 month),sessionstatusid=6,statuscode='limitexceed' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query21_779 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 day),sessionstatusid=6,statuscode='failed' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query22_783 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 year),sessionstatusid=6,statuscode='notauthorized' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query23_793 = ("UPDATE isphere.session SET sessionstatusid=7,captchaimage='".$res['result']['image']."' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query24_794 = ("UPDATE isphere.session SET captcha_id=NULL "
    #             "WHERE sessionstatusid=7 AND statuscode='used' AND id=" . $swapData['session'] -> id
    #             )

    # query25_799 = ("UPDATE isphere.session SET used=0,success=0,success_ext=ifnull(success_ext,0)+1,statuscode='success' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query26_803 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 day),sessionstatusid=6,statuscode='unknown' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query27_809 = ("UPDATE isphere.session SET used=0,success=0,success_ext=ifnull(success_ext,0)+1,statuscode='success' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query28_848 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 hour),sessionstatusid=6,statuscode='error' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )

    # query30_852 = ("UPDATE isphere.session SET unlocktime=date_add(now(),interval 1 hour),sessionstatusid=6,statuscode='empty' "
    #             "WHERE sessionstatusid=2 AND id=" . $swapData['session'] -> id
    #             )
