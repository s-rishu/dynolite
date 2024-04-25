package org.proj;

import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Initializer {
    static boolean failed = false;
    static KVStore hinted_store = new KVStore();
    static KVStore hosted_store = new KVStore();

    public static void main(String[] args) {
        try {

        } catch (Error e) {
            failed = true;
            e.printStackTrace();
            System.exit(-1);
        }
    }
}