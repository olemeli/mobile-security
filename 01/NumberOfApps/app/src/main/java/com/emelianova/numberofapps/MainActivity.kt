package com.emelianova.numberofapps

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        countApps()
    }

    private val rootingInstruments = listOf("com.thirdparty.superuser",
        "eu.chainfire.supersu",
        "com.noshufou.android.su",
        "com.koushikdutta.superuser",
        "com.zachspong.temprootremovejb",
        "com.ramdroid.appquarantine",
        "com.topjohnwu.magisk")

    private fun countApps() {
        val packageList = packageManager.getInstalledApplications(0)

        val nApps = packageList.size
        tvApps.text = getString(R.string.apps_message).format(nApps)

        var message = getString(R.string.not_found)
        for (pkg in packageList) {
            val pkgName = pkg.packageName
            if (rootingInstruments.contains(pkgName)) {
                message = getString(R.string.found)
                break
            }
        }
        rootInfo.text = message
    }
}
