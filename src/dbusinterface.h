/*
    Copyright (C) 2020 Sebastian J. Wolf and other contributors

    This file is part of Fernschreiber.

    Fernschreiber is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Fernschreiber is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Fernschreiber. If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef DBUSINTERFACE_H
#define DBUSINTERFACE_H

#include <QObject>
#include <QtDBus>

#include "dbusadaptor.h"

const QString INTERFACE_NAME = "org.ygriega.Fernschreiber";
const QString PATH_NAME = "/org/ygriega/Fernschreiber";

class DBusInterface : public QObject
{
    Q_OBJECT
public:
    explicit DBusInterface(QObject *parent = nullptr);
    DBusAdaptor *getDBusAdaptor();

signals:

public slots:

private:
    DBusAdaptor *dbusAdaptor;

};

#endif // DBUSINTERFACE_H
