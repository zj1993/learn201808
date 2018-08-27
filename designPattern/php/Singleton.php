<?php
//单例
class Singleton{
    //创建静态私有的变量保存该类对象
    private static $instance = null;
    //参数

    //防止直接创建对象
    private function __construct(){
        echo "我被实例化了";
    }
    //防止克隆对象
    private function __clone(){

    }
    static public function getInstance(){
        //判断$instance是否是Singleton的对象
        //没有则创建
        if (is_null(self::$instance)) {
            self::$instance = new Singleton;
        }
        return self::$instance;

    }

}
$db1 = Singleton::getInstance();
$db2 = Singleton::getInstance();

?>