package org.proj;

import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class InitRing {
    static int ring_size;
    public static void InitializeRing(int n) {
        for(int i = 0; i < n; i++) {
        }
    };
    public static void main(String[] args) {
        try {
            ring_size = Integer.parseInt(args[0]);

            InitializeRing(ring_size);
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }

    }
}